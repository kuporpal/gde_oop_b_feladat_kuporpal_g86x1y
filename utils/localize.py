class Localize:

    @staticmethod
    def get_text(kulcs, nyelv='hu'):
        locales = {
            'hu': {
                'menu_about': 'Névjegy',
                'menu_help': 'Súgó',
                'menu_file': 'Fájl',
                'menu_exit': 'Kilépés',
                'aboutmessage': 'Objektum Orientált Programozás \'B\' Beadandó Feladat\nRepülőjegy Foglalási Rendszer\nA programot készítette: Kupor Pál\nNeptun kód: G86X1Y',
                'windowtitle': 'Repülőjegy Foglalási Rendszer'
            },
            'en': {
                'menu_about': 'About',
                'menu_help': 'Help',
                'menu_file': 'File',
                'menu_exit': 'Exit',
                'aboutmessage': 'Object-Oriented Programming Assignment \'B\'\nFlight Ticket Booking System\nCreated by: Pál Kupor\nNeptun code: G86X1Y',
                'windowtitle': 'Flight Ticket Booking System'
            }
        }

        returnstring = locales.get(nyelv,locales['en']).get(kulcs,kulcs)

        return returnstring

