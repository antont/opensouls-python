/*NOTE: not used, 

just a note about a version with promise and exception handling,
from tobowers on DynamicsCompressorNode
*/
import { Soul, said } from "soul-engine/soul"

let resolve = () => {}

const main = async () => {
    const promise = new Promise((r) => (resolve = r))

    const soul = new Soul({
        organization: "antont",
        blueprint: "python",
    })
        
    soul.on("says", async ({ content }) => {
        console.log("Soul said", await content())
    })
        
    await soul.connect()

    await promise
}

main().then(() => console.log("done")).catch(console.error)