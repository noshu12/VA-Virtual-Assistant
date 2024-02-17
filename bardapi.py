from bardapi import Bard
import os 
import time



os.environ['_BARD_API_KEY'] = 'egiUkThsYAvru8p2XDbFsHsCpa2bG0RCp5A9rFRYP5sfjbTBNRD0KRyP_PBBCEKAh-YsVA'

query = "why is the sky is blue"

print(Bard().get_answer(str(query)))



