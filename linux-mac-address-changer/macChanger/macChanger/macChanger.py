import subprocess as sub
import optparse

optparser = optparse.OptionParser()

optparser.add_option("-i","--interface", dest = "interface",help = "interface change")
optparser.add_option("-m","--mac", dest = "newMac",help = "enter new mac address")

(user_inputs,arguments) = optparser.parse_args()
interface = user_inputs.interface
newMac = user_inputs.newMac

sub.call(["ifconfig",interface,"down"])
sub.call(["ifconfig",interface,"hw","ether",newMac])
sub.call(["ifconfig",interface,"up"])
print(f"mac address changed like {newMac}")
