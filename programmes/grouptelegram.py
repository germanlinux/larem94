from telethon import TelegramClient
import re
#MessageService(out=False, mentioned=False, media_unread=False, silent=False, post=False, id=247, from_id=190483374, to_id=PeerChannel(channel_id=1227208803), reply_to_msg_id=None, date=datetime.utcfromtimestamp(1514887801), action=MessageActionChatJoinedByLink(inviter_id=324578789))

# Use your own values here
api_id = 156792
api_hash = 'c67ae7fa9bbab7683277202b80abe02f'
phone_number = '+33681454398'

client = TelegramClient('postman', api_id, api_hash)
client.connect()
#print(client.is_user_authorized())
#client.send_code_request(phone_number)
#myself = client.sign_in(phone_number,'49226' )
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

dialogs, entities = client.get_dialogs(40)
for item in entities:
  if hasattr(item, 'title'):
     #print(item.title)
     if re.search('Boite',item.title):
        if  hasattr(item, 'megagroup'):
            entity  = item
#entity = entities[39]
#print(str(entities))
# (4) !! Invoking a request manually !!
result = client(GetHistoryRequest(
    entity,
    limit=50000,
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
    #print(str(m))
    if type(m) is Message:
       #print('---------------')
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
       #print("{} - {} - {}".format(prenom, nom,username ))
       chaine = f"{m.id};{prenom};{m.message};"
       ## recherche tag
       re_tag = r'#(\w+)'
       t_tag = re.findall(re_tag,m.message)
       if t_tag:
           tag = ";".join(t_tag)
           chaine += tag
           nchaine = re.sub(r'#(\w+)','',chaine)
           nchaine1 = re.sub(r'\n','',nchaine)

           print(nchaine1)
       listuser[prenom + ';' + nom +';' + username] = 1
'''
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
'''
exit()

offset = 0
limit = 200
all_participants = []
'''
while True:
    participants = client.invoke(GetParticipantsRequest(
        channel, ChannelParticipantsSearch(''), offset, limit
    ))
    if not participants.users:
        break
    all_participants.extend(participants.users)
    offset += len(participants.users)
    # sleep(1)  # This line seems to be optional, no guarantees!
'''
