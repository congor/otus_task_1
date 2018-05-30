import os
import ast
import collections
import nltk

nltk.download('averaged_perceptron_tagger')

def get_file_paths(project_path):
    filenames = []
    for dirname, dirs, files in os.walk(project_path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
            if len(filenames) == 100:
                break
    return filenames

def get_syntax_nodes(files_paths, with_filenames=False, with_file_content=False):
    nodes = []

    for file_path in files_paths:
        file_content = get_file_content(file_path)

        try:
            file_nodes = ast.parse(file_content)
        except SyntaxError:
            continue

        if with_filenames:
            if with_file_content:
                nodes.append((file_path, file_content, file_nodes))
            else:
                nodes.append((file_path, file_nodes))
        else:
            nodes.append(file_nodes)
    return nodes

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()

def get_functions_names(files_syntax_nodes):
    functions_names_list = [get_functions_from_node(file_nodes) for file_nodes in files_syntax_nodes]
    return make_list_flat(functions_names_list)

def get_functions_from_node(file_nodes):
    return [node.name.lower() for node in ast.walk(file_nodes) if (isinstance(node, ast.FunctionDef) and not is_special_marked(node.name))]

def is_special_marked(word):    
    return word.startswith('__') and word.endswith('__')

def get_verbs(functions_names):
    verb_lists = [verbs_from_function_name(function_name) for function_name in functions_names]
    return make_list_flat(verb_lists)

def verbs_from_function_name(function_name):
    words_function_name = function_name.split('_')
    words_function_name = [word for word in words_function_name if word != '']
    attached_tags = nltk.pos_tag(words_function_name)
    return [attached_tag[0] for attached_tag in attached_tags if 'VB' in attached_tag[1]]

def get_most_frequent_verbs(verbs, top_size=10):
    return collections.Counter(verbs).most_common(top_size)

def make_list_flat(_list):
    return sum(_list, [])

def determ_projects_locations(projects, test_folder):
    if os.path.isdir(os.path.join(test_folder)):        
        print('Internal test mode')
        return [os.path.join(test_folder, project) for project in projects]
    else:
        return projects
    
if __name__ == '__main__':
    test_folder = 'test_data'
    projects = [
        'django',
        'flask',
        'empty'
    ]

    projects = determ_projects_locations(projects, test_folder)

    verbs_statistics = []

    for project in projects:
        project_path = os.path.join(project)
        if not os.path.isdir(project_path):
            print("The project's folder '{}' is absent".format(project))
        files_paths = get_file_paths(project_path)
        files_syntax_nodes = get_syntax_nodes(files_paths)
        functions_names = get_functions_names(files_syntax_nodes)
        verbs = get_verbs(functions_names)
        verbs_statistics += get_most_frequent_verbs(verbs, 10)        

    [print(verb[0], verb[1]) for verb in get_most_frequent_verbs(verbs_statistics, 200)]