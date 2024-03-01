import { Soul, said } from "soul-engine/soul"
//i do this to deploy the lib directly in my python docker thing, but might be better to just use NPM there
//import { Soul, said } from "./node_modules/soul-engine/dist/soul/index.js" //SoulEnvironment

function initSoul(soulId, env, onConnect, onMessage, onLearned) {
  console.log("[initSoul] Env:", env);
  const soul = new Soul({
    soulId: soulId,
    organization: "antont",
    blueprint: "python",
    //environment: env,
    //token: "",
    //debug: true
  })
    
  soul.connect().then(async () => {
    console.log("Soul connected");
    //console.log(soul);
    //soul.dispatch(said("User", "Hi!"))
    onConnect();
    return soul;  
  });

  //content, perception
  /* custom message event, our app uses this kind of thing, and the discord bot served as an example
  soul.on("message", async (evt) => { //_metadata
    console.log(process.versions.node)
    const evt_json = JSON.stringify(evt)
    const evt2 = JSON.parse(evt_json)
    //console.log("Soul message EVT:", evt2)
    const says = await evt.content()
    const metadata = evt2.perception._metadata
    //const metadata = evt["perception"] //['_metadata']
    //console.log("Soul message PARSED:", says, metadata.repliedMessage)
    onMessage(says, metadata.repliedMessage)
  })
  */

  //normal soul-engine chat
  soul.on("says", async ({ content }) => {
    console.log("Soul says");
    const says = await content()
    console.log("Soul said:", says)
    onMessage(says)
  })

  soul.on("learnedAboutUser", async ({ content }) => {
    console.log("[learnedAboutUser]]");
    const learned = await content();
    console.log("Learned:", learned);
    onLearned(learned);
  })

  // soul.on("newPerception", (evt) => {
  //   console.log("PERCEPTION:", evt);
  // })

  return soul;
}

/*for making a custom event
function messaged(soul, message) {
  const msg_data = {
    action: "messaged",
    content: message.content,
    name: message.authorName,
    _metadata: {
      message: {
        id: message.id,
        roomId: message.roomId,
        authorId: message.authorId,
        username: message.authorName
      }
    }
  }
  //console.log("Sending Messaged:", msg_data)
  soul.dispatch(msg_data);
}
*/

export { initSoul, Soul, said } //messaged
