# _MAC Address Changer_

This python script changes your MAC Address temporarily on your GNU/Linux machine by this you can increase your anonymity.
All the changes will reset once you restart your computer.

### _How to do this manually?_
```
1. Open your terminal.
2. ifconfig <name-of-interface> down
3. ifconfig <name-of-interface> hw ether <your-temporary-MAC-address>
4. ifconfig <name-of-interface> up
```


### _How to use this script?_
```
1. Open your terminal.
2. sudo python3 mac_changer.py -i <name-of-interface> -m <your-temporary-MAC-address>
```
