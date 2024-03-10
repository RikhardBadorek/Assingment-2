import xmlrpc.client

client = xmlrpc.client.ServerProxy('http://localhost:3333')

while True:
    print("\nAdd notes or retrieve notes:")
    print("1. Add Note")
    print("2. Retrieve Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        topic = input("Enter topic: ")
        text = input("Enter text: ")
        response = client.add_or_update_note(topic, text)
        print(response)

    elif choice == '2':
        topic = input("Enter topic to retrieve notes: ")
        notes = client.retrieve_notes(topic)
        if notes:
            print("\nNotes:")
            for note in notes:
                print(f"\nText: {note['text']}\nTimestamp: {note['timestamp']}")
        else:
            print(f"No notes found for topic '{topic}'.")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
