from dotenv import load_dotenv
load_dotenv()

import argparse
import sys

from repo_loader import load_repo
from chunker import chunk_code
from embeddings import build_vector_store
from agent import create_agent


def parse_args():
    parser = argparse.ArgumentParser(
        description="🧠 Code Helper Agent - Analyze GitHub repositories with AI"
    )

    parser.add_argument(
        "--repo",
        type=str,
        required=True,
        help="GitHub repository URL (e.g. https://github.com/user/repo)"
    )

    return parser.parse_args()


def main():
    args = parse_args()
    repo_url = args.repo

    print("\n🚀 Code Helper Agent started\n")

    # 1️⃣ Repo yükle
    print(f"📥 Loading repository:\n   {repo_url}")
    try:
        documents = load_repo(repo_url)
    except Exception as e:
        print(f"\n❌ Failed to load repository:\n{e}")
        sys.exit(1)

    # 2️⃣ Chunking
    print("\n✂️  Chunking code...")
    try:
        chunks = chunk_code(documents)
    except Exception as e:
        print(f"\n❌ Chunking failed:\n{e}")
        sys.exit(1)

    # 3️⃣ Embeddings + Vector Store
    print("\n🧠 Building embeddings (this may take a minute)...")
    try:
        vector_store = build_vector_store(chunks)
    except Exception as e:
        print(f"\n❌ Embedding step failed:\n{e}")
        sys.exit(1)

    # 4️⃣ Agent oluştur
    agent = create_agent(vector_store)

    print("\n✅ Ready! Ask questions about the code.")
    print("Type 'exit' or 'quit' to stop.\n")

    # 5️⃣ CLI loop
    while True:
        question = input("❓ > ").strip()

        if not question:
            continue

        if question.lower() in {"exit", "quit"}:
            print("\n👋 Bye!")
            break

        try:
            answer = agent.invoke(question)
            print(f"\n🤖 {answer}\n")
        except Exception as e:
            print(f"\n❌ Error while answering:\n{e}\n")


if __name__ == "__main__":
    main()
