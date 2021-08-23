from random import choice
paises = [
    "Andorra",
    "Emiratos Árabes Unidos",
    "Afganistán",
    "Antigua y Barbuda",
    "Anguila",
    "Albania",
    "Armenia",
    "Antillas Holandesas",
    "Angola",
    "Antártida",
    "Argentina",
    "Samoa Americana",
    "Austria",
    "Australia",
    "Aruba",
    "Azerbaiyán",
    "Bosnia y Herzegovina",
    "Barbados",
    "Bangladesh",
    "Bélgica",
    "Burkina Faso",
    "Bahrein",
    "Burundi",
    "Benin",
    "Bermudas",
    "Bolivia",
    "Brasil",
    "Bahamas",
    "Bután",
    "Isla Bouvet",
    "Bulgaria",
    "Botswana",
    "Brunei",
    "Bielorrusia",
    "Belice",
    "Canadá",
    "República Centroafricana",
    "Congo",
    "Suiza",
    "Costa de Marfil",
    "Islas Cook",
    "Chile",
    "Camerún",
    "China",
    "Colombia",
    "Costa Rica",
    "Cuba",
    "Cabo Verde",
    "Isla de Navidad",
    "Chipre",
    "República Checa",
    "Alemania",
    "Djibouti",
    "Dinamarca",
    "Dominica",
    "República Dominicana",
    "Argelia",
    "Ecuador",
    "Estonia",
    "Egipto",
    "Sáhara Occidental",
    "Eritrea",
    "España",
    "Etiopía",
    "Finlandia",
    "Fiji",
    "Islas Malvinas",
    "Micronesia",
    "Islas Feroe",
    "Francia",
    "Gabón",
    "Reino Unido",
    "Granada",
    "Georgia",
    "Guayana Francesa",
    "Ghana",
    "Gibraltar",
    "Groenlandia",
    "Gambia",
    "Guinea",
    "Guadalupe",
    "Guinea Ecuatorial",
    "Grecia",
    "Georgia del Sur y Islas Sandwich del Sur",
    "Guatemala",
    "Guam",
    "Guinea-Bissau",
    "Guayana",
    "Hong Kong",
    "Islas Heard y McDonald",
    "Honduras",
    "Croacia",
    "Haití",
    "Hungría",
    "Indonesia",
    "Irlanda",
    "Israel",
    "India",
    "Territorio Británico del Océano Índico", 
    "Irak",
    "Irán",
    "Islandia",
    "Italia",
    "Jamaica",
    "Jordania",
    "Japón",
    "Kenia",
    "Kirguistán",
    "Camboya",
    "Kiribati",
    "Comoras",
    "Saint Kitts y Nevis",
    "Corea del Norte",
    "Corea del Sur",
    "Kuwait",
    "Las Islas Caimán",
    "Kazajstán",
    "Laos",
    "Líbano",
    "Santa Lucía",
    "Liechtenstein",
    "Sri Lanka",
    "Liberia",
    "Lesoto",
    "Lituania",
    "Luxemburgo",
    "Letonia",
    "Libia",
    "Marruecos",
    "Mónaco",
    "Moldavia",
    "Madagascar",
    "Islas Marshall",
    "Macedonia",
    "Malí",
    "Myanmar",
    "Mongolia",
    "Macao",
    "Islas Marianas del Norte",
    "Martinica",
    "Mauritania",
    "Montserrat",
    "Malta",
    "Mauricio",
    "Maldivas",
    "Malawi",
    "México",
    "Malasia",
    "Mozambique",
    "Namibia",
    "Nueva Caledonia",
    "Níger",
    "Norfolk Island",
    "Nigeria",
    "Nicaragua",
    "Países Bajos",
    "Noruega",
    "Nepal",
    "Nauru",
    "Niue",
    "Nueva Zelanda",
    "Omán",
    "Panamá",
    "Perú",
    "Polinesia francés",
    "Papua Nueva Guinea",
    "Filipinas",
    "Pakistán",
    "Polonia",
    "San Pedro y Miquelón",
    "Pitcairn",
    "Puerto Rico",
    "Portugal",
    "Palau",
    "Paraguay",
    "Qatar",
    "Reunión",
    "Rumania",
    "La Federación de Rusia",
    "Ruanda",
    "Arabia Saudita",
    "Las Islas Salomón",
    "Seychelles",
    "Sudán",
    "Suecia",
    "Singapur",
    "Santa Elena",
    "Eslovenia",
    "Svalbard y Jan Mayen",
    "República Eslovaca",
    "Sierra Leona",
    "San Marino",
    "Senegal",
    "Somalia",
    "Suriname",
    "Santo Tomé y Príncipe",
    "El Salvador",
    "Siria",
    "Swazilandia",
    "Islas Turcas y Caicos",
    "Chad",
    "Territorios del sur francés",
    "Togo",
    "Tailandia",
    "Tayikistán",
    "Tokelau",
    "Turkmenistán",
    "Túnez",
    "Tonga",
    "Timor Oriental",
    "Turquía",
    "Trinidad y Tobago",
    "Tuvalu",
    "Taiwan",
    "Tanzania",
    "Ucrania",
    "Uganda",
    "Reino Unido",
    "Islas menores de EE.UU.",
    "Estados Unidos de América",
    "Uruguay",
    "Uzbekistán",
    "Ciudad del Vaticano",
    "San Vicente y las Granadinas",
    "Venezuela",
    "Islas Vírgenes",
    "Vietnam",
    "Vanuatu",
    "Islas Wallis y Futuna",
    "Samoa",
    "Yemen",
    "Mayotte",
    "Yugoslavia",
    "Sudáfrica",
    "Zambia",
    "Zaire",
    "Zimbabue"
]

nombres = [
    "Carlos Marx",
    "Adam Smith",
    "Francisco Franco",
    "Niceto Alcalá-Zamora",
    "Manuel Azaña",
    "Sabino Arana",
    "Joaquín Sabina",
    "Rafa Nadal",
    "Monserrat Caballé",
    "Freddie Mercury",
    "Jeff Bezos",
    "Amancio Ortega",
    "Ortega y Gasset",
    "Ramón y Cajal",
    "Ash Ketchum",
    "Sans",
    "Gadafi",
    "Bin Ladden",
    "Largo Caballero",
    "Teemo",
    "Cristóbal Colón",
    "Blas de Lezo",
    "Isabel Díaz Ayuso",
    "Puigdemont",
    "Perro Sanxe",
    "Matteo Salvini",
    "José Antonio Primo de Rivera",
    "Miguel Primo de Rivera",
    "Emilio Mola",
    "José Antonio, Primo de Albert Rivera,",
    "Juan Carlos I",
    "Felipe VI",
    "Felpudo VI",
    "Felipe V",
    "Carlos II",
    "Rafael Alberti",
    "Antonio Machado",
    "Salvador Dalí",
    "Carmen Polo",
    "Froilán",
    "Día Sexto",
    "Lola Flores",
    "El Pequeño Nicolás",
    "Dolores Ibárruri",
    "Clara Ponsatí",
    "Clara Campoamor",
    "Esperanza Aguirre",
    "Carmen Calvo",
    "Nadia Calviño",
    "Dalas Review",
    "Ibai Llanos",
    "Vegetta777",
    "Mayichi",
    "Orslok",
    "Extremoduro",
    "Taburete",
    "Estopa",
    "La oreja de Van Gogh",
    "José Stalin",
    "Adolfo Hitler",
    "Vladimirio Lenín",
    "Benito Mussolini",
    "La Pegatina",
    "Rosalía",
    "Rosalía de Castro",
    "Julio César",
    "Cleopatra",
    "Pablo Echinque",
    "Santiago Abascal",
    "Toni Cantó",
    "José María Aznar",
    "Blas Cantó",
    "Felipe González",
    "Nicolás Maduro",
    "Carrero Blanco",
    "BasadoBot",
    "Pablo Iglesias Posse",
    "El Coletas",
    "Charmander",
    "Pablo Casado",
    "Irene Montero",
    "Hannah Montana",
    "Katy Perry",
    "Perry el ornitorrinco",
    "La CUP", 
    "Anatoli Karpov",
    "Magnus Carlsen",
    "Garry Kasparov",
    "David, el niño Antón,",
    "Jordi el niño polla",
    "David el gnomo",
    "Papa pitufo",
    "Gargamel",
    "D'Artagnan, el aprendiz de los tres mosqueteros,",
    "Gabriel García Márquez",
    "Juan Magán",
    "Luis Fonsi",
    "Camilo Sexto",
    "Jean Jungkook",
    "Aristóteles",
    "Gengis Kan",
    "Leonardo da Vinci",
    "Miguel de Cervantes",
    "Simón Bolívar",
    "Elon Musk",
    "PewDiePie",
    "Donald Trump",
    "Joe Biden",
    "Tracer, la de overwatch,",
    "Mercy, la de overwatch,",
    "Messi",
    "Cristiano Ronaldo",
    "Emmanuel Macron",
    "El primer ministro de la India",
    "Xi Jinping",
    "Winnie the Pooh",
    "Boris Johnson",
    "Margaret Thatcher",
    "Wiston Churchill",
    "Hirohito",
    "Camela",
    "El Albacete FC",
    "El equipo benjamín de fútbol de Granadilla de Abona, Canarias",
    "Pérez-Reverte",
    "Pedro Picapiedra",
    "Elvis Presley",
    "Julio Iglesias",
    "Miguel Bosé",
    "Kim Jong-Un",
    "Kim Yo-Jong",
    "King Kong",
    "Joseph Joestar",
    "Fran Perea",
    "Albert Pla",
    "Paco Sanz",
    "Alejandro Sanz",
    "Melendi",
    "Bambi",
    "Nelson Mandela"
]

todasLasFrases = [
    "{nombreuser} es un valor seguro",
    "Esto con {insertarnombre} no pasaba",
    "{insertarnombre} tiene el récord mundial en salto de altura",
    "{insertarnombre} tiene mil rosas para ti, {nombreuser}",
    "Sabes, yo conocí a {insertarnombre} antes de que fuera famoso",
    "{insertarnombre} se va de gira con Hatsune Miku",
    "{insertarnombre} es sus",
    "{insertarnombre} te ofrece un porro, ¿{nombreuser} aceptas?",
    "{insertarnombre} cree en la república independiente de Murcia",
    "{insertarnombre} es pambisitxs",
    "¡Suscríbete al onlyfans de {insertarnombre} por ₽9.99 ya mismo!",
    "{nombreuser} debe pilotar el EVA-01 o rei deberá hacerlo",
    "Estas en un coma, {nombreuser}, despiértate de la matrix",
    "Slava {insertarnombre}",
    "Si lees esto eres fan de {insertarnombre}",
    "Si eres pobre es por que quieres, mira a {insertarnombre} que empezó pobre como una rata",
    "{insertarnombre} ha desertado de Ciudadanos",
    "{insertarnombre} está planteándose comprar {pais}",
    "Rápido, {nombreuser}, {insertarnombre} va a hacer un golpe de estado, ¿lo apoyas?",
    "Viva Estopa",
    "EEUU está planteándose invadir {pais}",
    "{insertarnombre} te espera con la carita empapada, {nombreuser}",
    "{insertarnombre} ha volado por los aires",
    "{nombreuser}, te has encontrado con {insertarnombre} en un botellón, ¿que haces?",
    "{pais} será la próxima colonia española",
    "{insertarnombre} es inteligente, sé como {insertarnombre}",
    "{pais} sería mejor bajo la dictadura militar de {insertarnombre}",
    "{insertarnombre} ficha por el Barça",
    "Nuestro capitán revolucionario, {insertarnombre}, ha bendecido este post",
    "{insertarnombre} piensa que la tortilla es mejor sin cebolla",
    "Venga va, acabate las lentejas que los niños de África se comerían hasta la cuchara",
    "{insertarnombre} se está haciendo una racha de bajas en el LOL",
    "La primera bomba norcoreana va a ir a {pais}",
    "{insertarnombre} es un antivacunas",
    "Yo conozco un sitio que te ponen mejor tapa",
    "{nombreuser} delenda est",
    "{insertarnombre} es un agente doble norcoreano",
    "{insertarnombre} ha plantado la bomba",
    "{insertarnombre} se ha unido a los vengadores",
    "{insertarnombre} piensa que la tierra es plana",
    "Los gallegos son la clase dominante en todo el mundo",
    "Yo conozco uno que hace lo mismo pero a mitad de precio",
    "Con un 2-5 te digo yo que llevaba al Madrid a copa",
    "Plorareu",
    "Hay que trabajar más por que menos es imposible",
    "Los impuestos son un robo, mira a {insertarnombre}",
    "Los Simpsons predijeron a {insertarnombre}",
    "¡Ayuda por favor, no soy un bot, soy un niño venezolano que está contando los basados!",
    "{nombreuser} quiere un rey llamado Karl",
    "Habemus papam, {insertarnombre}",
    "{insertarnombre} lidera la III República Española",
    "{nombreuser} sacame de latinoamérica, estoy cansado de {pais}",
    "{insertarnombre} está planteándose comprar {pais}",
    "{insertarnombre} es criminal de guerra",
    "Españoles, {insertarnombre} ha muerto",
    "Mmm patas",
    "Si es que con {insertarnombre} se vivía mejor",
    "{insertarnombre} te invita a una partida al LOL, ¿aceptas {nombreuser}?",
    "{nombreuser} dígame su nombre, que le voy a apuntar un 0",
    "Spain is different",
    "{insertarnombre} estará en el proximo arco de jojo's",
    "Se debería hacer más rule34 de {insertarnombre}",
    "{nombreuser} tiene pornografía de {insertarnombre}",
    "{nombreuser} es nivel 107 en el LOL",
    "Me cago en la madre de {insertarnombre}",
    "El himno de España será compuesto por {insertarnombre}",
    "{insertarnombre} tiene un testículo más grande que el otro",
    "Odio mi vida...",
    "{insertarnombre} cree que su motorola es un espía del gobierno",
    "Sí, utilizo ese pantalón",
    "No hará mucho frio ahí",
    "Que grande {insertarnombre}",
    "¿Tengo que continuar la canción?",
    "¿Tampoco pasa nada, sabes?",
    "No, no necesito calcetines",
    "Joder, esos son un montón de calcetines",
    "Muchas gracias",
    "Eh, ¿cómo? {insertarnombre} ha vuelto",
    "Me van a tirar la torre...",
    "{insertarnombre} ha participado en los atentados del 11-S",
    "{insertarnombre} quiere jugar al Among Us en la vida real",
    "A {insertarnombre} le gustaría ser un furry",
    "Ojalá {insertarnombre} fuera mi padre",
    "¡Viva {pais}!",
    "{insertarnombre} no era tan malo",
    "Me da igual que la gente se esté matando",
    "Te han matado {nombreuser}, pero tienes 3000 de oro y puedes revivir",
    "Hey, you're finally awake {nombreuser}",
    "¡{pais}!",
    "El poder reside en las matemáticas",
    "A trabajar en una obra os ponía yo...",
    "No he entenido ni una palabra de toda esta jerga",
    "Con {insertarnombre} no había tantas chorradas",
    "{nombreuser} busca pareja, interesados al DM.",
    "Joder {pais} es mucho mas grande de lo que me imaginaba",
    "Con mi poderoso Mouse Gaming soy poderesisimo en el Ajedrez",
    "Sabía que no me podía fiar de {insertarnombre}",
    "Maduritas calientes en tu zona {nombreuser}",
    "Vendo opel corsa",
    "Friendship ended with {nombreuser}, now {insertarnombre} is my best friend",
    "{nombreuser} tiene un cuerno de mamut",
    "-¡Hola, {nombreuser}!\n+¡Hola, {insertarnombre}!\n-¿Vió usted a mi abuela?\n+A su abuela yo la ví.\n-Tengo fimosis"
]

def generador_frase(nombreuser):
    frase = choice(todasLasFrases)
    if choice(range(25)) == 0:
        frase = frase.replace("{insertarnombre}", nombreuser)

    else:
        frase = frase.replace("{insertarnombre}", choice(nombres))
    
    frase = frase.replace("{nombreuser}", nombreuser)
    frase = frase.replace("{pais}", choice(paises))
    if frase[-1] not in [".", "?", "!"]:
        if frase[-1] == ",":
            frase[-1] == "."

        else:
            frase += "."

    else:
        if frase[-2] == ",":
            del frase[-2]

    return frase