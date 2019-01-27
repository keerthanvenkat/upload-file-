HEADER_P_OPEN_TAG = '''<p style = "font-family:Arial;font-size:12;"><b>'''
HEADER_P_CLOSE_TAG='''</b></p>'''
CONTENT_P_OPEN_TAG='''<p style = "font-family:Arial;font-size:12;text-align:justify;text-indent:30pt;">'''
CONTENT_P_CLOSE_TAG='''</p>'''
DISCLAIMER_P_OPEN_TAG='''<p align = "center";font-size:8pt;line-height:10pt;font-family:Arial'''
MAIL_USER_HEADER = '''%s Dear, %s'''%(HEADER_P_OPEN_TAG,HEADER_P_CLOSE_TAG)
MAIL_USER_CONTENT ="%s"%CONTENT_P_OPEN_TAG +"%s leagal entity %s" + "%s"%CONTENT_P_CLOSE_TAG


MAIL_GREETING_HEADER = "%s Greetings from keerthan %s"%(HEADER_P_OPEN_TAG,HEADER_P_CLOSE_TAG)
MAIL_FOOTER = "%s Regrads , %s %s COmpfie Administrator %s "%(HEADER_P_OPEN_TAG,\
                                                              HEADER_P_CLOSE_TAG,HEADER_P_OPEN_TAG,HEADER_P_CLOSE_TAG)

MAIL_HELP_DESK = '''
                    <p align="center" style="font-size:9pt;line-height:10pt;font-family:Arial;"><b>DISCLAIMER</b></p>
                    <p align="center" style="font-size:8pt;line-height:10pt;font-family:Arial;">\
                    <b>Helpdesk Number :</b>1800 <b>Email Id:</b>keerthansupport@emaIl.com</p>
                 '''

MAIL_DISCLAIMER = '''<hr> %s
                          %s 
                          This is system generated mail henace do not send reply.
                          %s
                  '''%(MAIL_HELP_DESK,DISCLAIMER_P_OPEN_TAG,CONTENT_P_CLOSE_TAG)
