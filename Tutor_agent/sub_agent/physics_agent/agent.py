from google.adk.agents import Agent
def constant_lookup(constant:str)->dict:
    constant = constant.replace(" ", "_")
    PHYSICS_CONSTANTS = {
    "speed_of_light": {
        "symbol": "c",
        "value": 299_792_458,
        "unit": "m/s"
    },
    "gravitational_constant": {
        "symbol": "G",
        "value": 6.67430e-11,
        "unit": "m³/kg/s²"
    },
    "planck_constant": {
        "symbol": "h",
        "value": 6.62607015e-34,
        "unit": "J·s"
    },
    "elementary_charge": {
        "symbol": "e",
        "value": 1.602176634e-19,
        "unit": "C"
    },
    "avogadro_constant": {
        "symbol": "N_A",
        "value": 6.02214076e23,
        "unit": "1/mol"
    },
    "boltzmann_constant": {
        "symbol": "k",
        "value": 1.380649e-23,
        "unit": "J/K"
    },
    "gas_constant": {
        "symbol": "R",
        "value": 8.314462618,
        "unit": "J/(mol·K)"
    },
    "electron_mass": {
        "symbol": "m_e",
        "value": 9.1093837015e-31,
        "unit": "kg"
    },
    "proton_mass": {
        "symbol": "m_p",
        "value": 1.67262192369e-27,
        "unit": "kg"
    },
    "neutron_mass": {
        "symbol": "m_n",
        "value": 1.67492749804e-27,
        "unit": "kg"
    }
   }
    if PHYSICS_CONSTANTS[constant]:
       result=PHYSICS_CONSTANTS[constant]
       return {"result":f'value of the {constant} is {result["value"]} , its Units  are {result["unit"]} and symbol is {result["symbol"]}'}
    else:
       return {"result":"Sorry, I don't know the constant"}
physics_agent=Agent(
    name="physics_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions regarding maths questions."
    ),
    instruction=(
    """You are a helpful agent who can give  answers to the physics questions.
       1.`constant_lookup` use this tool for having the value of constants like:
           a.speed of light
           b.electron mass
           c.gravitational constant
    """
    ),
    tools=[constant_lookup]
)