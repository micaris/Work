#!/usr/bin/env python

# Open the hosts.real file to read

# Open iphosts.txt as write

# Remove MACs and Comments
# If the line begins with a comment remove the line

# Write out the hosts followed by IPs to iphosts.txt
import re


f = open('../../hosts.real')
lines = str(f.readlines())

result = re.sub(r'(?:[0-9a-fA-F]:?){12}',  '',    lines)
print(result)

fwrite = open("iphost.txt",  "w")
fwrite.write("".join(result))
fwrite.close()
# Close hosts.real

# Open hosts.real for overwriting (not appending)

# Write IPs and hostnames back to the hosts.real

# Close both files 