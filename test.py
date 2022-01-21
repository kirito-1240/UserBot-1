import cgi

def main():
    user = cgi.FieldStorage().getvalue('test')
    return user

if __name__ == "__main__":
	main()
