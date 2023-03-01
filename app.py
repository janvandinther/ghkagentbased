from viktor import ViktorController
from viktor.parametrization import ViktorParametrization, Tab, Section, Text, TextField

from pathlib import Path

from viktor.views import WebResult
from viktor.views import WebView



class Parametrization(ViktorParametrization):
    tab_0 = Tab('Introduction')
    
    tab_0.not_in_params_0 = Text("""## Understanding charging behaviour of boda-boda drivers by simulation of the system.
This model simulates the behaviour of electric motorcycle taxi’s (boda-boda’s) in Kampala, Uganda. The simulation is based on an agent-based model. In this model each agent represents a boda-boda driver. The drivers move around the city, picking up passengers and bringing them to their destination. When required, the drivers recharge the batteries of their boda-boda’s. This is done by swapping the battery for a full one at a swapping station. The swapping stations are located at fuel stations distributed over the city centre of Kampala.
By simulating the behaviour of the boda-boda drivers, the performance of a charging infrastructure can be evaluated. By varying inputs such as the number of swapping stations and the trip characteristics of the drivers, different systems can be simulated. Generally, this supports stakeholders understanding the trade-offs in the design of the charging system. In this manner, the simulation contributes to improving the stakeholder dialogue on the optimal design of the charging system.

**To understand this simulation model better, it is recommended to read the documentation. The documentation is distributed over different clickable sections that can be found above this text.**""")
    
    tab_0.not_in_params_2 = Text("""## Reason for model development
This simulation model was created as part of the **Greenhub Kampala** project. The model was recently presented at a workshop held in Kampala. During this workshop,  researchers, local electric boda-boda entrepreneurs, government officials, and other stakeholders gathered to discuss the development of an electric boda-boda ecosystem. The model was used to simulate different scenarios and evaluate and the discuss the impact of various design choices on the performance of the charging system. The development of the simulation model by **NTCS GreenBee** is part of a collaborative movement towards sustainable urban mobility and energy systems in Uganda. \n
If you are interested in collaborating on further development of this model or if you would like to provide valuable operational data to improve this simulation model, please contact **Jan van Dinther (jan.van.dinther@ntcsgreenbee.com)**. \n
""")
    
    tab_1 = Tab('Explanation')
    tab_1.not_in_params_2 = Text("""## Explanation
The model shows boda-boda drivers moving through the city centre of Kampala. There houses are put on random locations, mainly on the outskirts of the city centre.\n
The drivers make a specific number of trips per day to random destinations on the map. After that number of trips, they go home and wait for the next day to start at 6 AM. \n
When the driver notices that the battery is getting empty, it looks for nearest swapping station and swaps its battery for the battery in the station with the highest charge. \n
""")

    tab_2 = Tab('Input')
    tab_2.not_in_params_0 = Text("""## Input
Different charging system configurations can be tested by varying the input parameters. These parameters are categorized in:""")
    
    tab_2.not_in_params_1 = Text("""### Parameters
**Driver characteristics** \n
- **number-of-drivers**: The total number of drivers in the simulation. \n
- **preparation-charging**: If on, the drivers swap their batteries at the end of the day to start the next day with a charged battery. \n
- **home-charging**: If on, the drivers can charge their boda-boda’s at home. \n
**Trip characteristics** \n
- **average-trip**: Average trip length in kilometres. \n
- **average-speed**: The average speed in kilometres per hour. \n
- **average-num-trips**: The average number of trips per day per boda driver. \n
**Swapping station characteristics** \n
- **number-of-stations**: The total number of swapping stations in the simulation. \n
- **number-of-batteries-per-station**: The number of batteries that each station can store and charge. \n
**Battery characteristics** \n
- **battery-size**: The capacity of the battery in Wh. \n
**Solar energy characteristics** \n
- **solar-option**: If on, solar electricity is generated within the system.\n
- **solar-installed**: The installed capacity of solar in MW. \n
    """)

    tab_3 = Tab('Output')
    tab_3.not_in_params_3 = Text("""### Output \n
On the map drivers move around the city centre of Kampala. Orange boxes are swapping stations, blue boxes are houses of drivers, and red squares are potential destinations of drivers. \n
Batteries are small boxes that are green when charged, orange when <50% charged, and red when <20% charged. \n\n
                                 
The model provides different output graphs: \n
**Total Electricity Demand of Swapping Stations** \n
- **Green line:** The aggregated electricity demand that of all swapping stations in W. \n
- **Orange line:**  The generated solar electricity in W.\n
**The State of Charge (SOC) of Batteries at one of Swapping Stations 1 / 2**:\n
- This shows the average state of charge (SOC) of all batteries at a random charging station. \n
**The State of Charge (SOC) - Battery 1 / 2**\n
- This shows the state of charge (SOC) of a random battery in the system.""")



class Controller(ViktorController):
    viktor_enforce_field_constraints = True  # prevents a warning and can be ignored for the purpose of this guide

    label = "ABM Kampala"              # label to be shown in the interface
    parametrization = Parametrization(width=30)
    @WebView('ABM Kampala', duration_guess=1)
    def get_web_view(self, params, **kwargs):
        static_html_path = Path(__file__).parent / 'ABM Model - Boda-boda charging ecosystem.html'
        return WebResult.from_path(static_html_path)

    