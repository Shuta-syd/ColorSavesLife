from    disability_assistant \
        import  DisabilityAssistant

from    plugins.color_disability.color_disability \
        import  ColorDisability

def main(args=None):
    disability_assitant = DisabilityAssistant()
    disability_assitant.plugin_master.togglePlugin(ColorDisability())

    disability_assitant.start()

if  __name__ == "__main__":
    main()
    
