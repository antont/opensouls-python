import javascript

#just to trigger npm install .. as can't import /soul ?
#soul_engine = javascript.require('soul-engine')
# print(soul_engine)
js_socialengine = javascript.require('./soulengine.mjs')
soul_engine = js_socialengine #workaround the path import fail

print(soul_engine)

Soul = soul_engine.Soul
said = soul_engine.said
initSoul = soul_engine.initSoul
#messaged = soul_engine.messaged
print("Python Soulengine exports:", Soul, said, initSoul)
