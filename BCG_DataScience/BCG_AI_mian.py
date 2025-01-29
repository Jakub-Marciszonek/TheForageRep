from BCG_AI_Queries import SimpleChatbot as SC

list =[]

def main():
    print("~~~~~~~Welcome in simple commend driven buissnes data display~~~~~~~")
    print("To get to know possible commends type help")
    while True:
        Action = ""
        Command = input("\n>").lower().strip().split()
        try:
            Action = Command[0]
        except:
            print("No command")
        try:
            args = [Command[1]+" "+Command[2]]

            for i in range(4, len(Command), 2):
                args.append(Command[i])
        except:
            args = ["placeholder"]

        if not "Action" in locals():
            continue
        elif Action == "exit":
            print("Goodbye c:")
            break
        elif Action == "help":
            SC(args).HelpDisplay()
        elif Action == "viewf":
            SC(args).ViewFigure()
        elif Action == "comparechange":
            SC(args).CompareChange()
        elif Action == "comparecompanies":
            SC(args).CompareCompanies()
        elif Action == "adata":
            SC(args).AvailableData()
        elif Action == "afigures":
            SC(args).AvailableFigures()
        else:
            print("Unknown command: <action>. Type \'help\' for \
instructions")
            
main()