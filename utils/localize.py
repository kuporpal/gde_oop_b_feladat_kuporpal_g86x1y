class Localize:

    @staticmethod
    def get_text(kulcs, nyelv='hu'):
        locales = {
            'hu': {
                'menu_about': 'Névjegy',
                'menu_help': 'Súgó',
                'menu_file': 'Fájl',
                'menu_exit': 'Kilépés',
                'about_message': 'Objektum Orientált Programozás \'B\' Beadandó Feladat\nRepülőjegy Foglalási Rendszer\nA programot készítette: Kupor Pál\nNeptun kód: G86X1Y',
                'window_title': 'Repülőjegy Foglalási Rendszer',
                'exit_button': ' Kilépés a programból',
                'exit_alert': 'Biztosan be akarja zárni a programot?',
                'international_flight': 'Nemzetközi Járat',
                'domestic_flight': 'Belföldi Járat'
            },
            'en': {
                'menu_about': 'About',
                'menu_help': 'Help',
                'menu_file': 'File',
                'menu_exit': 'Exit',
                'about_message': 'Object-Oriented Programming Assignment \'B\'\nFlight Ticket Booking System\nCreated by: Pál Kupor\nNeptun code: G86X1Y',
                'window_title': 'Flight Ticket Booking System',
                'exit_button': ' Exit from the booking system',
                'exit_alert': 'Are You sure to exit the program?',
                'international_flight': 'International Flight',
                'domestic_flight': 'Domestic Flight'
            }
        }

        returnstring = locales.get(nyelv,locales['en']).get(kulcs,kulcs)

        return returnstring

