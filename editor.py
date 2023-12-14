import auto_editor.edit as edit
import auto_editor.ffwrapper as ffwrapper
import auto_editor.validate_input as validator
import auto_editor.utils.func as edit_funcs
import auto_editor.utils.log as edit_log

finished = False

def CutFile(input_path : str, export_type : str = None):
    my_args = edit.Args(input=[input_path],export=export_type) # set out input

    # setting ffmpeg to use it later (there's nothing fancy here..)
    ffmpeg = ffwrapper.FFmpeg(
            my_args.ffmpeg_location,
            my_args.my_ffmpeg,
            my_args.show_ffmpeg_commands,
            my_args.show_ffmpeg_output,
        )

    #the same thing again
    temp = edit_funcs.setup_tempdir(my_args.temp_dir, edit_log.Log())

    #the same thing again
    log = edit_log.Log(my_args.debug, my_args.quiet, temp=temp)
    log.debug(f"Temp Directory: {temp}")

    #validating our file first
    paths = validator.valid_input(my_args.input, ffmpeg, my_args, log)
    #start the editing process
    edit.edit_media(paths, ffmpeg, my_args, temp, log)
    pass

def CuttingProgress():
    return finished