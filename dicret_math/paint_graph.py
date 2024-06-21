S = [[0, 4, 6, 1, 5, 10],
     [4, 0, 0, 0, 3, 0],
     [6, 0, 0, 0, 0, 2],
     [1, 0, 0, 0, 8, 9],
     [5, 3, 0, 8, 0, 7],
     [10, 0, 2, 9, 7, 0]]
dict_vertex = dict()
vector = []
dict_count_vertex = dict()
mass_of_vertexes = []
used_vertex = []
def find_vertexes(S):
     help_mass = []
     for i in range(len(S)):
          for j in range(len(S[0])):
               if S[i][j] > 0:
                    help_mass.append(f"x{j}")
          dict_vertex[f"x{i}"] = help_mass
          mass_of_vertexes.append(f"x{i}")
          help_mass = []
find_vertexes(S)
print(dict_vertex)
def takeFirst(elem):
     return elem[0]
def takeSecond(elem):
     return elem[1]
def build_vector(my_dict):
     for key, value in my_dict.items():
          dict_count_vertex[key] = len(value)
     sorted_vertex = [[k, v] for k, v in dict_count_vertex.items()]
     sorted_vertex.sort(key=takeSecond, reverse=True)
     for i in range(len(sorted_vertex)):
          vector.append(takeFirst(sorted_vertex[i]))
     print("Vector", vector)
def paint_graph(vector):
     help_mass = []
     dict_paints = dict()
     p = 1
     for el in vector:
          temporary_mass = dict_vertex.get(el)
          for i in range(len(mass_of_vertexes)):
               if mass_of_vertexes[i] not in temporary_mass and mass_of_vertexes[i] not in used_vertex:
                    help_mass.append(mass_of_vertexes[i])
                    used_vertex.append(mass_of_vertexes[i])
          dict_paints[f"color{p}"] = help_mass
          help_mass = []
          if len(used_vertex) == len(mass_of_vertexes):
               break
          p += 1
     print("Словарь красок: ", dict_paints)
     print(f"Всего понадобилось красок: {p}")
build_vector(dict_vertex)
paint_graph(vector)
