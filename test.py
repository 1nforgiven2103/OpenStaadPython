
from openstaad import *




# print("Start Testing...")
# print('-'*20+'\nGeometry node Functions\n'+'-'*20)

# ## GEOMETRY - NODE
# node_1 = 1
# node_2 = 2
# cordidinates = (0.0, 0, 0.0)
# print('- GetLastNodeNo')
# print(geometry.GetLastNodeNo())

# print('- GetNodeCoordinates')
# print(geometry.GetNodeCoordinates(node_1))

# print('- GetNodeCount')
# print(geometry.GetNodeCount())

# print('- GetNodeDistance')
# print(geometry.GetNodeDistance(node_1,node_2))

# print('- GetNodeIncidence')
# print(geometry.GetNodeIncidence(node_1))

# print('- GetNodeList')
# print(geometry.GetNodeList()[0:10])

# print('- GetNodeNumber')
# print(geometry.GetNodeNumber(cordidinates))

# print('- GetNoOfSelectedNodes')
# print(geometry.GetNoOfSelectedNodes())

# print('- GetSelectedNodes')
# print(geometry.GetSelectedNodes()[0:10])

# # ## GEOMETRY - BEAM

# print('-'*20+'\nGeometry beam Functions\n'+'-'*20)

# beam_1 = 1
# print('- GetBeamLength')
# print(geometry.GetBeamLength(beam_1))

# print('- GetBeamList')
# print(geometry.GetBeamList()[0:10])

# print('- GetLastBeamNo')
# print(geometry.GetLastBeamNo())

# print('- GetMemberCount')
# print(geometry.GetMemberCount())

# print('- GetMemberIncidence')
# print(geometry.GetMemberIncidence(beam_1))

# print('- GetNoOfSelectedBeams')
# print(geometry.GetNoOfSelectedBeams())

# print('- GetSelectedBeams')
# print(geometry.GetSelectedBeams()[0:10])

# print('- GetNoOfBeamsConnectedAtNode')
# print(geometry.GetNoOfBeamsConnectedAtNode(node_1))

# print('- GetBeamsConnectedAtNode')
# print(geometry.GetBeamsConnectedAtNode(node_1))

# # ## GEOMETRY - GROUP

# print('-'*20+'\nGeometry group Functions\n'+'-'*20)

# group_1 = '_BEAMS'
# print('- GetGroupEntityCount')
# print(geometry.GetGroupEntityCount(group_1))

# print('- GetGroupEntities')
# print(geometry.GetGroupEntities(group_1)[0:10])

# # print("\nPROPERTIES FUNCTIONS\n")

# print('-'*20+'\nProperties Functions\n'+'-'*20)

# print('- GetBeamSectionName')
# print(properties.GetBeamSectionName(beam_1))

# print('- GetBeamSectionPropertyRefNo')
# print(properties.GetBeamSectionPropertyRefNo(beam_1))

# print('- GetSectionPropertyValues')
# print(properties.GetSectionPropertyValues(4))

# print('- GetMemberSpecCode')
# print(properties.GetMemberSpecCode(424))

# # ## ROOT FUNCTIONS 

# print('-'*20+'\nRoot Functions\n'+'-'*20)

# print('- GetAnalysisStatus')
# print(root.GetAnalysisStatus())

# print('- GetApplicationVersion')
# print(root.GetApplicationVersion())

# print('- GetBaseUnit')
# print(root.GetBaseUnit())

# print('- GetInputUnitForForce')
# print(root.GetInputUnitForForce())

# print('- GetInputUnitForLength')
# print(root.GetInputUnitForLength())

# print('- GetSTAADFile')
# print(root.GetSTAADFile())

# print('- GetSTAADFile')
# print(root.GetSTAADFile(bFullPath=False))

# print('- GetSTAADFileFolder')
# print(root.GetSTAADFileFolder())

# ## OUTPUT FUNCTIONS

# print('-'*20+'\nOutput Functions\n'+'-'*20)

# print('- GetMemberEndForces')
# print(output.GetMemberEndForces(beam=beam_1, start=False, lc=1, local = 1))

# print('- GetSupportReactions')
# print(output.GetSupportReactions(node_1))

# print('-'*20+'\nLoad Functions\n'+'-'*20)

# print('- GetLoadCaseTitle')
# print(load.GetLoadCaseTitle(lc=1))


# from openstaad import Root, Geometry,Load,Output,Properties, Support, View


# root = Root()
def has_loads(load_data):
    return any(len(x) > 0 for x in load_data)

def parse_udl_load(udl_tuple):
    """
    Convierte un tuple de UDL en un diccionario legible:
    - direction: índice de dirección (0=X_local, ..., 5=Y_global, ...)
    - magnitude: valor de la carga
    - D1, D2, D3: desplazamientos / offsets
    """
    if not udl_tuple or len(udl_tuple) < 5:
        return None

    direction, magnitude, d1, d2, d3 = udl_tuple

    return {
        "direction_index": direction[0] if direction else None,
        "magnitude": magnitude[0] if magnitude else 0,
        "D1": d1[0] if d1 else 0,
        "D2": d2[0] if d2 else 0,
        "D3": d3[0] if d3 else 0
    }

def parse_concentrated_load(conc_tuple):
    """
    Convierte un tuple de concentrated load en un diccionario legible:
    - direction_index: índice de la dirección de la carga
    - magnitude: valor de la carga
    - D1, D2: desplazamientos o offsets
    """
    if not conc_tuple or len(conc_tuple) < 4:
        return None

    direction, magnitude, d1, d2 = conc_tuple

    return {
        "direction_index": direction[0] if direction else None,
        "magnitude": magnitude[0] if magnitude else 0,
        "D1": d1[0] if d1 else 0,
        "D2": d2[0] if d2 else 0
    }


def parse_nodal_load(nodal_tuple):
    """
    Convierte un tuple de nodal load en un diccionario legible:
    - Fx, Fy, Fz: fuerzas
    - Mx, My, Mz: momentos
    """
    if not nodal_tuple or len(nodal_tuple) < 6:
        return None

    fx, fy, fz, mx, my, mz = nodal_tuple

    return {
        "Fx": fx[0] if fx else 0,
        "Fy": fy[0] if fy else 0,
        "Fz": fz[0] if fz else 0,
        "Mx": mx[0] if mx else 0,
        "My": my[0] if my else 0,
        "Mz": mz[0] if mz else 0
    }

staad_path1="C:\\Users\\ccarvajal\\Downloads\\Staad_to_SACS\\Staad\\test_to_sacs.std"


root = Root(staad_path1)
geometry=Geometry(staad_path1)
load=Load(staad_path1)
output=Output(staad_path1)
properties=Properties(staad_path1)
support=Support(staad_path1)
view=View(staad_path1)

geometry.GetMemberIncidence
count_lc=load.GetPrimaryLoadCaseCount()
load_cases=list(load.GetPrimaryLoadCaseNumbers())
beam_list=geometry.GetBeamList()
node_list=geometry.GetNodeList()

load_cases_data = {}

for load_case in load_cases:
    load.SetLoadActive(load_case)

    load_case_title = load.GetLoadCaseTitle(load_case)
    load_type_code = load.GetLoadType(load_case)

    item_load_count = load.GetLoadItemsCount(load_case)
    load_items = []

    for item_load in range(item_load_count):
        load_item_type = load.GetLoadItemType(load_case, item_load)

        if not load_item_type or load_item_type == "Unknown Load Item Type":
            continue

        load_items.append(load_item_type)

    nodal_loads = {}

    for node in node_list:
        node_load = load.GetNodalLoads(node)
        node_load_parsed=parse_nodal_load(node_load)

        if not has_loads(node_load):
            continue

        nodal_loads[node] = {
            "loads": node_load_parsed
        }

    beam_loads = {}

    for beam in beam_list:
        udl_load = load.GetUDLLoads(beam)
        udl_load_parsed=parse_udl_load(udl_load)
        conc_load = load.GetConcForces(beam)
        conc_load_parsed=parse_concentrated_load(conc_load)

        if not has_loads(udl_load) and not has_loads(conc_load):
            continue

        beam_loads[beam] = {
            "udl": udl_load_parsed,
            "concentrated": conc_load_parsed
        }

    load_cases_data[load_case] = {
        "title": load_case_title,
        "type": load_type_code,
        "items": load_items,
        "nodal_loads": nodal_loads,
        "beam_loads": beam_loads,
    }

print(load_cases_data)
