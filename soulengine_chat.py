"""
Simple minimal version of soul-engine use from python over the JS bridge.

A cut-down version of our actual module which uses async queues and locking for a multi-user server.
If there's interest, we could develop this open source thing to include that too,
or maybe that could an alternative version.
"""

import time
import soulengine

#we have an async multi-user server so it has this kind of things,
#disabled here for simplicity / clarity at least for now
# connect_queue = asyncio.Queue()

def on_connect():
    pass
#     connect_queue.put_nowait('') #TODO: multiuser

# def says_in_room(room: ChatRoom):
#     #assert room.id not in says
#     queue = asyncio.Queue()
#     says[room.id] = queue

said: str | None = None

def on_said(content):
    print("Python callback / message:", content)
    global said
    said = content

def on_learned(content):
    print("Learned about User")
    print(content)

def init_soul(
    #env: SoulEnv
    ) -> soulengine.Soul:
    # conn = soul.connect()
    # print("Then:", conn.then)
    #failed to do callback stuff over the bridge, doing it in js now
    
    #print("Env for Soul:", env)

    soul = soulengine.initSoul(
        None,
        None, #env.model_dump(),
        on_connect,
        on_said,
        on_learned,
    )
    return soul

def say(soul, content: str):
    soul.dispatch(
        soulengine.said(
            "User", content
        )
    )
    print("User said:", content)

    # says_value = await says.get()
    # content, replied_message = says_value
    # while not says[room.id].empty():
    #     discard = await says[room.id].get()
    #     print("WARNING - Discarded AI says:", discard)
    #     #XXX TODO get all messages
    # #print("Says:", says_value)


#async 
def runtest():
    # env = SoulEnv(
    #     soulName="ChatSoulDEV",
    #     soulInstructions="Be nice, be respectful",
    #     playerName="MrUnknown"
    # )

    soul = init_soul() #env

    print("[soulengine_chat test] #1")
    #ret1 = await 
    say(soul, "What's up?")
    #print(ret1)

    while True:
        if said is None:
            time.sleep(0.1)
        else:
            break
    print("[runtest] Said:", said)
    
    # print("[soulengine_chat test] #2")    
    # ret2 = await say_in_room(
    #     room, #type: ignore
    #     "What's your name?"
    #     )
    # #print(ret2)

    # print("[soulengine_chat test] #3")
    # ret3 = await say_in_room(
    #     room, #type: ignore
    #     "I'm the Test Man"
    #     )
    # #print(ret3)

    # print("[soulengine_chat test] #4")
    # ret4 = await say_in_room(
    #     room, #type: ignore
    #     "The best tests in the world. For Chat NPCs, you know!"
    #     )
    # #print(ret4)

    # #it takes time for the Soul to learn about the user
    # await asyncio.sleep(15)
    
if __name__ == '__main__':
    #asyncio.run(runtest())
    runtest()
