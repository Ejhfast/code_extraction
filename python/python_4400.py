# Restrict a regex to only search between two points
import retext = "[Customer01]\nName: Mr Smith\nAddress: Somewhere\nTelephone: 01234567489\n[Customer02]\nName: Mr Jones\nAddress: Laandon\nTelephone:\n[Customer03]\nName: Mr Brown\nAddress: Bibble\nTelephone: 077764312"blah = re.search("[Customer02]\nName:\s*(.*?)\n", text)print blah.group(1)
