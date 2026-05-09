import time
fn='chemdata.txt'
da={}
def data():
    with open(fn,'r') as f:
        for i in f:
            key,value=i.strip().split(':')
            da[key.lower()]=value
def adddata():
    print("""--Format to write data(follow or sys. will break)--
<keyword-to-get-data>:<data-to-store>
IMPORTANT use seprator ':' to seprate keyword and data""")
    print('-'*60)
    d=input('Enter data you want to add:\n')
    with open (fn,'a') as f:
        f.write(d+'\n')
        print('----Data was added successfully')
    print('-'*60)
def bot(user):
    data()
    user = user.lower()
    responses = []
    for key, value in da.items():
        if key in user:
            responses.append(value)
    if responses:
        return "\n".join(responses)
    return "I don't know this yet."
def chat():
    print("🔄 Initializing system...")
    time.sleep(1)
    print("📡 Loading data...")
    time.sleep(1)
    print("✅ READY!\n")
    print("🤖 Chatbot (type 'exit' to quit)\n-(add to 'add' new data)")
    while True:
        user = input("You: ").lower()
        if user.lower() == "exit" or user.lower() == 'bye':
            print("Bot: Goodbye!")
            break
        elif user.lower() == 'add':
            adddata()
            continue
        print("🤖 Thinking...")
        time.sleep(1)
        response =bot(user)
        print("Bot:", response)
chat()