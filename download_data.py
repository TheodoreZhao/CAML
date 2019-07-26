from hdfs import InsecureClient
import os
client = InsecureClient("http://10.150.144.225:50070", user = "v-kanzha")
client.download("/SC_recommendation/caml/Electronics_new_strategy_new_2","data/", overwrite=True)
print(os.listdir("data/"))
