import shutil
import os
import gui



def move_files_with_pattern(src_folder, dest_folder, pattern):
            global size
            # Create the destination folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            list_of_files = os.listdir(src_folder)
                
            size = len(list_of_files)
            num_of_files_moved=0
            # Iterate over files in the source folder    
            for index in range(size):
                src_filepath = os.path.join(src_folder, list_of_files[index])
                    
                    # Check if the file name contains "pattern"
                if pattern in list_of_files[index]:
                    dest_filepath = os.path.join(dest_folder, list_of_files[index])
                    num_of_files_moved += 1

                        # Move the file to the destination path
                    shutil.move(src_filepath, dest_filepath)
                    print(f"Moved: {list_of_files[index]} to {dest_folder}")
                gui.progress_animation(index, size)
                
            gui.stop_spinner()
            gui.show_popup(num_of_files_moved)