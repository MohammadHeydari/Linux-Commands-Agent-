from llm import ask_llm
from executor import run_tool

def run_agent():

    while True:
        user_input = input("\nEnter your query: ")

        tool_obj = ask_llm(user_input)

        print("\nLLM:", tool_obj)

        tool = tool_obj.get("tool", "none")
        args = tool_obj.get("args", {})

        if tool == "none":
            print("\nNo tool selected. stopping.")
            continue

        print(f"\n[Running]: {tool}")

        output = run_tool(tool, args)

        print(f"\n🎯 FINAL: {output}")


if __name__ == "__main__":
    run_agent()