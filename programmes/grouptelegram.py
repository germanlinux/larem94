from telethon import TelegramClient

# Use your own values here
api_id = 156792
api_hash = 'XXXXXX'
phone_number = '+33XXXXXX'

client = TelegramClient('postman', api_id, api_hash)
client.connect()
#print(client.is_user_authorized())
#client.send_code_request(phone_number)
#myself = client.sign_in(phone_number,'XXXXX' )
#print(client.is_user_authorized())
#from telethon.tl.functions.contacts import ResolveUsernameRequest
#result = client(ResolveUsernameRequest('jeanenmarche'))
#found_chats = result.chats
#found_users = result.users
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty,Message,InputUser
from telethon.tl.functions.messages import GetHistoryRequest
myself = client.get_me()
#print(myself)
#lonami  = client.get_entity('jeanenmarche')
total, messages, senders = client.get_message_history('GERMANLINUX')
#print( str(messages))

dialogs, entities = client.get_dialogs(10)
entity = entities[8]
#print(str(entities))
# (4) !! Invoking a request manually !!
result = client(GetHistoryRequest(
    entity,
    limit=5000,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0
))

# Now you have access to the first 20 messages
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import PeerUser
messages = result.messages

listuser= {}
for m in messages:
   # print(str(m))
    if type(m) is Message:
       print('---------------')
       my_userexp    = client.get_entity(PeerUser(m.from_id))
       #my_userexp    = client.get_input_entity(PeerUser(m.from_id))
       if my_userexp.first_name:
            prenom = my_userexp.first_name
       else:
            prenom=''
       if my_userexp.last_name:
            nom = my_userexp.last_name
       else:
            nom=''

       if my_userexp.last_name:
            username = my_userexp.last_name
       else:
            username =''
       print("{} - {} - {}".format(prenom, nom,username ))
       print(m.message)
       listuser[prenom + ';' + nom +';' + username] = 1
print('**************************')
print(len(messages))
print(len(listuser))
for l in listuser:
    print(l)
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest
#updates = client(ImportChatInviteRequest('FdFg1Eeb6JlTxdEecc_zEw'))
#https://t.me/joinchat/FdFg1Eeb6JlTxdEecc_zEw
#print(str(updates))
exit()

offset = 0
limit = 200
all_participants = []

while True:
    participants = client.invoke(GetParticipantsRequest(
        channel, ChannelParticipantsSearch(''), offset, limit
    ))
    if not participants.users:
        break
    all_participants.extend(participants.users)
    offset += len(participants.users)
    # sleep(1)  # This line seems to be optional, no guarantees!
