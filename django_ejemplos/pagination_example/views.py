# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    context = RequestContext(request)
    data = {}
    data['food_list'] = [
        {'name': u'Albondigas'},
        {'name': u'Bisteces de Res Encebollado'},
        {'name': u'Bisteces de Res en Mole de Cacahuate'},
        {'name': u'Bisteces de Res en Salsa de Mostaza'},
        {'name': u'Bisteces de Res en Salsa Pasilla'},
        {'name': u'Carne de Cerdo con Chile'},
        {'name': u'Carne en su Jugo'},
        {'name': u'Cola en Mole de Olla'},
        {'name': u'Costillitas de Cerdo a la Barbicure'},
        {'name': u'Costillitas de Cerdo con Piña'},
        {'name': u'Costillas de Cerdo al Vapor'},
        {'name': u'Chamorro de Cerdo en Achiote'},
        {'name': u'Chicharron con Chile'},
        {'name': u'Chiles Rellenos de Carne'},
        {'name': u'Espinazo de Res'},
        {'name': u'Filetes de Res con Platano, Piña y Cebolla'},
        {'name': u'Filete de Ternera con Cebollas'},
        {'name': u'Ubre en Mole de Olla'},
        {'name': u'Lengua de Res en Salsa Roja'},
        {'name': u'Lomo Borracho'},
        {'name': u'Lomo de Cerdo Adobado'},
        {'name': u'Milanesas de Res Empanizadas'},
        {'name': u'Pacholas'},
        {'name': u'Picadillo'},
        {'name': u'Rollo de Carne al Horno'},
        {'name': u'Albóndigas de Pescado'},
        {'name': u'Almejas a la Mexicana'},
        {'name': u'Bacalao a la Mexicana'},
        {'name': u'Bacalao al Vino Tinto'},
        {'name': u'Bacalao Campestre'},
        {'name': u'Bocadillos de Atún'},
        {'name': u'Bocadillos de Sardina'},
        {'name': u'Caldo de Mariscos'},
        {'name': u'Caldo de Pescado'},
        {'name': u'Camarones en Salsa Verde'},
        {'name': u'Cebiche'},
        {'name': u'Huachinango a la Veracruzana'},
        {'name': u'Pastel Azteca de Sardinas'},
        {'name': u'Patee de Pescado'},
        {'name': u'Pescado Adobado'},
        {'name': u'Pescado en Salsa Verde'},
        {'name': u'Tortas de Atún'},
        {'name': u'Tortas de Camarón'},
        {'name': u'Tostadas de Cazón Molido'},
        {'name': u'Mole Dulce'},
        {'name': u'Molotes de Pollo'},
        {'name': u'Pechugas de Pollo Rellenas'},
        {'name': u'Pollo a la Mantequilla'},
        {'name': u'Pollo Almendrado'},
        {'name': u'Calabacitas Rellenas'},
        {'name': u'Chiles Rellenos de Queso'},
        {'name': u'Chiles Rellenos de Queso y Elote'},
        {'name': u'Chiles Rellenos en Escabeche'},
        {'name': u'Enchiladas'},
        {'name': u'Enchiladas Potosinas'},
        {'name': u'Frijoles de la Olla'},
        {'name': u'Migas'},
        {'name': u'Pastel Azteca'},
        {'name': u'Pambazos'},
        {'name': u'Papas asadas rellenas de Chicharos'},
        {'name': u'Pozole'},
        {'name': u'Rajitas de Chile Poblano'},
        {'name': u'Sopa de Tortilla'},
        {'name': u'Sopes'},
        {'name': u'Tacos al Pastor'},
        {'name': u'Tacos al Vapor de Frijoles'},
        {'name': u'Tacos al Vapor de Papas'},
        {'name': u'Tacos al Vapor de Carne'},
        {'name': u'Tacos Dorados'},
        {'name': u'Tacos de Labio de Res'},
        {'name': u'Tamales Oaxaqueños'},
        {'name': u'Tortas de Papa'},
        {'name': u'Bocadillos de Huevo y Jamón'},
        {'name': u'Ejotes con Huevo'},
        {'name': u'Huevos enrollados con jamón'},
        {'name': u'Huevos rellenos de Atún'},
        {'name': u'Nopales con Huevo'},
        {'name': u'Papas con Huevo'},
        {'name': u'Sopa de Arroz Blanco'},
        {'name': u'Sopa de Arroz Blanco con Chiles'},
        {'name': u'Sopa de Arroz Rojo'},
        {'name': u'Sopa de Aguacate con jamón'},
        {'name': u'Sopa de Elote'},
        {'name': u'Sopa de Flor de Calabaza'},
        {'name': u'Sopa de Garbanzos con nopales'},
        {'name': u'Sopa de Lentejas'},
        {'name': u'Sopa de Papa'},
        {'name': u'Sopa de Pescado'},
        {'name': u'Crema de Aguacate'},
        {'name': u'Crema de Aguacate al Tequila'},
        {'name': u'Crema de Berros'},
        {'name': u'Crema de Camote'},
        {'name': u'Crema de Camarón con hoja santa'},
        {'name': u'Crema de Chayotes'},
        {'name': u'Crema de Champiñones'},
        {'name': u'Crema de Coliflor'},
        {'name': u'Crema de Espinacas'},
        {'name': u'Crema de Frijoles'},
        {'name': u'Crema de Flor de Calabaza'},
        {'name': u'Crema de Macarrones'},
        {'name': u'Crema de Mariscos'},
        {'name': u'Crema de Nopales'},
        {'name': u'Crema de Pepinos'},
        {'name': u'Arroz con Leche'},
        {'name': u'Brazo Gitano'},
        {'name': u'Cacahuates Grapiñados'},
        {'name': u'Camotes Poblanos'},
        {'name': u'Empanadas de Leche'},
        {'name': u'Empanadas de Mermelada'},
        {'name': u'Dulce de Platano'},
        {'name': u'Flan Envinado'},
        {'name': u'Galletas Tipo Empanadas'},
        {'name': u'Gelatina de Ciruela Pasa'},
        {'name': u'Gelatina de Kalúa'},
        {'name': u'Gelatina de Rompope'},
        {'name': u'Guayabas en Almíbar'},
        {'name': u'Jamoncillos de Piñon'},
        {'name': u'Leche Envinada'},
        {'name': u'Mantecadas de Zanahoria'},
        {'name': u'Mermelada de Tejocote'},
        {'name': u'Natillas'},
        {'name': u'Naranjas Rellenas'},
        {'name': u'Nieve de Nuez'},
        {'name': u'Pan de Elote'},
        {'name': u'Panque de Natas con Pasitas'},
        {'name': u'Plátanos Flameados'},
        {'name': u'Polvorones de Naranja'},
        {'name': u'Postre de Manzana'},
    ]
    data['food_number_per_page'] = 10
    template_name = "pagination_example.html"
    return render_to_response(template_name, data, context_instance=context)