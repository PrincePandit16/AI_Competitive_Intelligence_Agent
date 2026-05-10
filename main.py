from app.graph.workflow import workflow

if __name__ == "__main__":

    query = "Analyze Nvidia AI strategy"

    response = workflow.invoke({"query":query})

    print("\n")
    print("=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    print(response["summary"])

    print("\n")
    print("=" * 80)
    print("VERIFICATION REPORT")
    print("=" * 80)

    print(response["verification_report"])



    print("\n")
    print("=" * 80)
    print("FINAL REPORT")
    print("=" * 80)

    print(response["final_report"])