class Parser:
    FILE_NAME_INDEX = 0

    @staticmethod
    def get_accounts(args):
        args.pop(Parser.FILE_NAME_INDEX)
        return args
