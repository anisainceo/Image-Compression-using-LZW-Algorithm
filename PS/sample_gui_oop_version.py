from    PIL         import  Image, ImageTk  # --> Used for image i/o operations. 
from    tkinter     import  filedialog      # --> Used for file dialog box on "Open & Save".
from    tkinter     import  ttk             # --> Used for GUI widgets.
import  tkinter     as      tk              # --> Used for GUI super class.
import  numpy       as      np              # --> Used for image array operations.
import  os                                  # --> Used for file and directory operations.

class Application(tk.Tk) :
    """Class, that inherits from tk.Tk, and is used to create the GUI."""

    def __init__(self, *args:list, **kwargs:dict) -> None:
        """
        Constructor method for the Application class which utilizes the GUI initialization.
        @params:
            *args : (list) : (Optional) : List of arguments to be passed to the tk.Tk.__init__ method.
            **kwargs : (dict) : (Optional) : Dictionary of keyword arguments to be passed to the tk.Tk.__init__ method.
        @returns:
            None
        """
        super().__init__(*args, **kwargs) # --> Call the tk.Tk.__init__ method to initialize the GUI.
        
        self.style = ttk.Style() # --> Create a ttk.Style object to be used for styling the GUI. (Optional)
        self.style.theme_use("clam") # --> Set the theme of the GUI to "clam". (Optional)

        self.title("Image Proccesser - Default") # --> Set the title of the GUI.
        
        self.work_dir = os.getcwd() # --> Get the current working directory.
        self.image_file_path = os.path.join(self.work_dir, "thumbs_up.bmp") # --> Set the default image file path.
        try : # --> Try to open the image file. If it fails, then set the image as default black.
            self.original_image = Image.open(self.image_file_path) # --> Open the image file.
            self.temporary_image = Image.open(self.image_file_path) # --> Open the image file.
        except : # --> If the image file fails to open, then set the image as default black.
            self.image_file_path = None # --> Set the image file path to None.
            self.original_image = Image.new('RGB', (256, 256), (0, 0, 0)) # --> Create a new black image.
            self.temporary_image = Image.new('RGB', (256, 256), (0, 0, 0)) # --> Create a new black image.
        self.original_reference = ImageTk.PhotoImage(self.original_image) # --> Create a PhotoImage object from the original image. !!! This is used for displaying image ! The PhotoImage literally losses image data.
        self.temporary_reference = ImageTk.PhotoImage(self.temporary_image) # --> Create a PhotoImage object from the temporary image.

        self.columnconfigure(0, weight=1) # --> Configure the column to be weight 1. Which means it will expand to fill the window.
        self.rowconfigure(0, weight=1) # --> Configure the row to be weight 1. Which means it will expand to fill the window.

        self.container = ttk.Frame(self, padding=5) # --> Create a ttk.Frame object to be used as the container for the GUI.
        self.container.grid(row=0, column=0) # --> Place the container in the GUI. Wıth configured grids. It will stay on the middle in as the gui expands.

        self.container.columnconfigure((0,1,2,3), weight=1) # --> Configure the columns to be weight 1. Which means they will expand to fill the window.
        self.container.rowconfigure((0,1,2,3,4), weight=1) # --> Configure the rows to be weight 1. Which means they will expand to fill the window.

        original_title_label = ttk.Label(self.container, text="Original Image", anchor="center") # --> Create a ttk.Label object to be used as the title for the original image.
        original_title_label.grid(row=0, column=0, columnspan=2) # --> Place the original title label in the container.

        temporary_title_label = ttk.Label(self.container, text="Temporary Image", anchor="center") # --> Create a ttk.Label object to be used as the title for the temporary image.
        temporary_title_label.grid(row=0, column=2, columnspan=2) # --> Place the temporary title label in the container.

        self.original_photo_label = ttk.Label(self.container, image=self.original_reference, anchor="center") # --> Create a ttk.Label object to be used as the label for the original image.
        self.original_photo_label.grid(row=1, column=0, columnspan=2) # --> Place the original photo label in the container.

        self.temporary_photo_label = ttk.Label(self.container, image=self.temporary_reference, anchor="center") # --> Create a ttk.Label object to be used as the label for the temporary image.
        self.temporary_photo_label.grid(row=1, column=2, columnspan=2) # --> Place the temporary photo label in the container.

        self.original_info_label = ttk.Label(self.container) # --> Create a ttk.Label object to be used as the label for the original image info.
        self.original_info_label.grid(row=2, column=0, columnspan=2) # --> Place the original info label in the container.
        self.__update_photo_info_label("original") # --> Update the original info label.

        self.temporary_info_label = ttk.Label(self.container) # --> Create a ttk.Label object to be used as the label for the temporary image info.
        self.temporary_info_label.grid(row=2, column=2, columnspan=2) # --> Place the temporary info label in the container.
        self.__update_photo_info_label("temporary") # --> Update the temporary info label.

        self.ask_file_button = ttk.Button(self.container, text="Open Image", command=self.__load_file) # --> Create a ttk.Button object to be used as the button for opening a new image file.
        self.ask_file_button.grid(row=3, column=0, columnspan=1) # --> Place the ask file button in the container.

        self.reset_image_button = ttk.Button(self.container, text="Reset Image", command=self.__reset_image) # --> Create a ttk.Button object to be used as the button for resetting the image.
        self.reset_image_button.grid(row=3, column=1, columnspan=2) # --> Place the reset image button in the container.

        self.save_file_button = ttk.Button(self.container, text="Save Image", command=self.__save_file) # --> Create a ttk.Button object to be used as the button for saving the image.
        self.save_file_button.grid(row=3, column=3, columnspan=1) # --> Place the save file button in the container.

        self.proccess_gray_scale_button = ttk.Button(self.container, text="Gray Scale", command=lambda: self.__procces_conversion()) # --> Create a ttk.Button object to be used as the button for proccessing the image as gray scale.
        self.proccess_gray_scale_button.grid(row=4, column=0, columnspan=1) # --> Place the proccess gray scale button in the container.

        self.proccess_red_button = ttk.Button(self.container, text="Red", command=lambda: self.__procces_conversion(0)) # --> Create a ttk.Button object to be used as the button for proccessing the image as red.
        self.proccess_red_button.grid(row=4, column=1, columnspan=1) # --> Place the proccess red button in the container.

        self.proccess_green_button = ttk.Button(self.container, text="Green", command=lambda: self.__procces_conversion(1)) # --> Create a ttk.Button object to be used as the button for proccessing the image as green.
        self.proccess_green_button.grid(row=4, column=2, columnspan=1) # --> Place the proccess green button in the container.

        self.proccess_blue_button = ttk.Button(self.container, text="Blue", command=lambda: self.__procces_conversion(2)) # --> Create a ttk.Button object to be used as the button for proccessing the image as blue.
        self.proccess_blue_button.grid(row=4, column=3, columnspan=1) # --> Place the proccess blue button in the container.

        for child in self.container.winfo_children() : # --> Iterate through all the children of the container. To apply general changes to all of them respectively.
            child.grid_configure(padx=5, pady=5, sticky='nsew') # --> Configure the children to have a padding of 5 pixels in both x and y directions. And to be sticky to the north, south, east and west directions.
        
    def __reset_image(self) -> None:
        """
        Method, that resets the temporary image to the original image.
        @params:
            None
        @returns:
            None
        """
        original_image = self.original_image # --> Get the original image.
        self.temporary_image = original_image # --> Create a new PhotoImage object from the original image.
        self.temporary_reference = ImageTk.PhotoImage(self.temporary_image) # --> Create a new PhotoImage object from the temporary image.
        self.temporary_photo_label.configure(image=self.temporary_reference) # --> Configure the temporary photo label to use the new PhotoImage object.
        self.__update_photo_info_label("temporary") # --> Update the temporary info label.
        
    def __procces_conversion(self, color_index:int=None) -> None:
        """
        Method, that handles the conversation operations, gray-scale | red | green | blue.
        @params:
            color_index : (int) : (Optional) : (Default = None) : Selection of the color to be converted. In RGB space.
        @returns:
            None
        """
        rgb_image = self.original_image # --> Get the original image.
        
        if color_index is None : # --> If the color index is None, then the image is converted to gray-scale.
            gray_image = rgb_image.convert('L') # --> Convert the image to gray-scale.
            self.temporary_image = gray_image # --> Create a new PhotoImage object from the gray-scale image.
        else :
            rgb_image = self._pil_to_np(rgb_image) # --> Convert the image to a numpy array.
            rgb_image[:,:,np.where(np.arange(3) != color_index)] = 0 # --> Set all the pixels of the colors that are not the selected color to 0.
            rgb_image = self._np_to_pil(rgb_image) # --> Convert the numpy array back to a PIL image.
            self.temporary_image = rgb_image # --> Create a new PhotoImage object from the converted image.

        self.temporary_reference = ImageTk.PhotoImage(self.temporary_image) # --> Create a new PhotoImage object from the temporary image.
        self.temporary_photo_label.configure(image=self.temporary_reference) # --> Configure the temporary photo label to use the new PhotoImage object.
        self.__update_photo_info_label("temporary") # --> Update the temporary info label.

    def __load_file(self) -> None:
        """
        Method, that handles the loading of the image file.
        @params:
            None
        @returns:
            None
        """
        self.ask_file_button.configure(state='disabled', text='Loading Image') # --> Disable the ask file button, and change the text to Loading Image.

        input_file_path = filedialog.askopenfile(initialdir = self.work_dir, title = 'Select an image file', filetypes = [('png files', '*.png')]) # --> Open a file dialog to select an image file.

        if input_file_path : # --> If the input file path is not None, then the user selected a file.
            self.image_file_path = input_file_path.name # --> Get the file path of the selected file.

            file_name = os.path.basename(self.image_file_path) # --> Get the file name of the selected file.
            self.title(f"Image Proccesser - {file_name}") # --> Set the title of the window to the file name.

            self.original_image = Image.open(self.image_file_path) # --> Create a PhotoImage object from the selected image file.
            self.original_reference = ImageTk.PhotoImage(self.original_image) # --> Create a new PhotoImage object from the original image.
            self.original_photo_label.configure(image=self.original_reference) # --> Configure the original photo label to use the new PhotoImage object.
            self.__update_photo_info_label("original") # --> Update the original info label.

            self.temporary_image = Image.open(self.image_file_path) # --> Create a new PhotoImage object from the selected image file.
            self.temporary_reference = ImageTk.PhotoImage(self.temporary_image) # --> Create a new PhotoImage object from the temporary image.
            self.temporary_photo_label.configure(image=self.temporary_reference) # --> Configure the temporary photo label to use the new PhotoImage object.
            self.__update_photo_info_label("temporary") # --> Update the temporary info label.

        self.ask_file_button.configure(state='normal', text='Open Image') # --> Enable the ask file button, and change the text to Open Image.

    def __save_file(self) -> None:
        """
        Method, that handles the saving of the image file.
        @params:
            None
        @returns:
            None
        """
        self.save_file_button.configure(state='disabled', text='Saving Image') # --> Disable the save file button, and change the text to Saving Image.

        output_file_path = filedialog.asksaveasfilename(initialdir = self.work_dir, title = 'Select an image file', filetypes = [('png files', '*.png')]) # --> Open a file dialog to select an image file.

        if output_file_path : # --> If the output file path is not None, then the user selected a file.
            
            if not output_file_path.endswith('.png') : # --> If the output file path does not end with .png, then add it.
                output_file_path += '.png' # --> Add .png to the output file path.

            output_image = self.temporary_image # --> Get the temporary image.
            output_image.save(output_file_path) # --> Save the temporary image to the selected file.
        
        self.save_file_button.configure(state='normal', text='Save Image') # --> Enable the save file button, and change the text to Save Image.

    def __update_photo_info_label(self, label_id:str) -> None:
        """
        Method, that updates the photo info label.
        @params:
            label_id : (str) : (Required) : The id of the label to be updated.
        @returns:
            None
        """
        if label_id == "original" : # --> If the label id is original, then update the original info label.
            photo_info = self._get_image_info(self.original_image) # --> Get the image info of the original image.
            self.original_info_label.configure(text=photo_info, anchor="center") # --> Configure the original info label to display the image info.
        elif label_id == "temporary" : # --> If the label id is temporary, then update the temporary info label.
            photo_info = self._get_image_info(self.temporary_image) # --> Get the image info of the temporary image.
            self.temporary_info_label.configure(text=photo_info, anchor="center") # --> Configure the temporary info label to display the image info.
        else :
            print("Invalid label id.") # --> If the label id is not original or temporary, then print an error message.
            return # --> If the label id is not original or temporary, then terminate method.

    def _get_image_info(self, image:Image) -> str:
        """
        Method, that returns the image info.
        @params:
            image : (PIL.Image) : (Required) : The image to be processed.
        @returns:
            (str) : The image info.
        """
        image_array = self._pil_to_np(image) # --> Convert the PIL image to a numpy array.

        image_width = image_array.shape[1] # --> Get the width of the image.
        image_height = image_array.shape[0] # --> Get the height of the image.
        image_channels = image_array.ndim # --> Get the number of channels of the image.

        to_return = f"Size : {image_width}  x {image_height}, Dimensions : {image_channels}" # --> Create the image info string.

        return to_return # --> Return the image info string.

    def _pil_to_np(self, image:Image) -> np.array:
        """
        Method, that converts a PIL image to a numpy array.
        @params:
            image : (PIL.Image) : (Required) : The image to be converted.
        @returns:
            (np.array) : The converted image.
        """
        return np.array(image) # --> Return the converted image.

    def _np_to_pil(self, image_array:np.array) -> Image:
        """
        Method, that converts a numpy array to a PIL image.
        @params:
            image_array : (np.array) : (Required) : The image to be converted.
        @returns:
            (PIL.Image) : The converted image.
        """
        return Image.fromarray(np.uint8(image_array)) # --> Return the converted image.

if __name__ == '__main__' : # --> Prevents when other modules import this module, the code below is not executed.

    Application().mainloop() # --> Executing application with objectless approach.