"""This is what I did first to use the open-source socialagi lib"""

import javascript
#from pydantic import BaseModel, ConfigDict

socialagi = javascript.require('socialagi')
js_socialagi = javascript.require('./js_socialagi/main.mjs')

ChatMessageRoleEnum = socialagi.ChatMessageRoleEnum
CortexStep = socialagi.CortexStep
externalDialog = socialagi.externalDialog
internalMonologue = socialagi.internalMonologue

createMessage = js_socialagi.createMessage

def chat():
    """porting examples/metacognition.ts"""

    print(socialagi)
    print("* -- *")
    print(js_socialagi)


    #note: it should work to generate these types from the ts interfaces using
    #https://pypi.org/project/ts2python/
    # class ChatMessage(BaseModel):
    #     role: str #ChatMessageRoleEnum
    #     content: str

    #     #model_config = ConfigDict(arbitrary_types_allowed=True)
    #this leads to error about unexpected param ffid ending up in the GPT request, due to the bridge

    initial_memory = [
        # ChatMessage(
        #     role=ChatMessageRoleEnum.System,
        #     content="Hi"
        # )
        createMessage(
            ChatMessageRoleEnum.System,
            "Hi"
        )
    ]

    dialog = CortexStep("BotName");
    dialog = dialog.withMemory(initial_memory);
    #print(dialog)
    says = dialog.next(externalDialog());
    print(says)

if __name__ == '__main__':
    chat()

"""
ooh this works, we get:

CortexStep {
  memories: [
    { role: 'system', content: 'Hi' },
    {
      role: 'assistant',
      content: 'BotName said: "Hello! How can I assist you today?"'
    }
  ],
  lastValue: 'Hello! How can I assist you today?',
  entityName: 'BotName',
(...)
"""

#intermediate_thought_process = ["pondered how she feels", "wondered about intention"];


