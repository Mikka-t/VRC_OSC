from asari.api import Sonar

def analyze(word):
    sonar=Sonar()
    info = sonar.ping(text= word)
    ans=[0,0]
    ans[0] = info["classes"][0]["confidence"] ## negative
    ans[1] = info["classes"][1]["confidence"] ## positive
    print(ans)
    print(info["top_class"])
    return ans