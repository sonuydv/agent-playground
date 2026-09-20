from agent_demo.agent import run_agent


def main():

    print("Mini Agent")
    print("Type 'exit' to quite.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        answer =  run_agent(user_input)
        print(f"\n Agent: {answer}\n")

if __name__ == "__main__":
    main()
