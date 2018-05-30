import unittest
import os
import projects_functions_verbs as tested_project


class TestCountVerbsMethods(unittest.TestCase):

    def test_files_paths_from_path(self):
        test_path = 'test_data/django'
        file_names = tested_project.get_file_paths(os.path.join(test_path))
        file_names.sort()
        self.assertEqual(file_names, [os.path.join(test_path,'__init__.py'),
                                      os.path.join(test_path,'error.py'),
                                      os.path.join(test_path,'make.py'),
                                      os.path.join(test_path,'test.py')]
                         )
        test_path = 'test_data/empty'
        file_names = tested_project.get_file_paths(os.path.join(test_path))
        self.assertEqual(file_names, [(os.path.join(test_path, '__init__.py'))])

    def test_function_names_from_path(self):
        path = os.path.join('test_data/django')
        files_paths = tested_project.get_file_paths(path)
        files_syntax_nodes = tested_project.get_syntax_nodes(files_paths)
        function_names = tested_project.get_functions_names(files_syntax_nodes)
        self.assertEqual(function_names, ['give_give', 'timer', 'make', 'get', 'take'])

    def test_verbs(self):
        list_to_filter = ['give_give', 'timer', 'make', 'get', 'take']
        filtered_list = tested_project.get_verbs(list_to_filter)
        self.assertEqual(filtered_list, ['give', 'make', 'get', 'take'])
        
    def test_list_flat(self):
        complicated_list = [[1, 2, 3], [4, 5], [6]]
        flat_list = tested_project.make_list_flat(complicated_list)
        self.assertEqual(flat_list, [1, 2, 3, 4, 5, 6])
        
if __name__ == '__main__':
    unittest.main(exit=False)