# This file pulls from the CD Catalog,
# makes arrays for the items in the catalog,
# and then displays the information to the user


def check_amounts(xmldoc):
    a = int(0)
    b = int(0)
    c = int(0)
    d = int(0)
    e = int(0)
    f = int(0)
    g = open('cd_catalog.xml')
    lines = g.readlines()
    cd_catalog = "cd_catalog.xml"
    word = str("<CD>")
    with open(cd_catalog, 'r') as g:
        for line in g:
            words = line.split()
            for i in words:
                if(word in i):
                    a = a + 1
    cd_amount = a
    word = str("<TITLE>")
    with open(cd_catalog, 'r') as g:
        for line in g:
            words = line.split()
            for i in words:
                if(word in i):
                    b = b + 1
    title_amount = b
    word = str("<ARTIST>")
    with open(cd_catalog, 'r') as g:
        for line in g:
            words = line.split()
            for i in words:
                if(word in i):
                    c = c + 1
    artist_amount = c
    word = str("<COUNTRY>")
    with open(cd_catalog, 'r') as g:
        for line in g:
            words = line.split()
            for i in words:
                if(word in i):
                    d = d + 1
    country_amount = d
    word = str("<PRICE>")
    with open(cd_catalog, 'r') as g:
        for line in g:
            words = line.split()
            for i in words:
                if(word in i):
                    e = e + 1
    prices_amount = e
    word = str("<YEAR>")
    with open(cd_catalog, 'r') as g:
        for line in g:
            words = line.split()
            for i in words:
                if(word in i):
                    f = f + 1
    year_amount = f
    if(a == b == c == d == e == f):
        return a
    else:
        print("There is information missing from the catalog.")


def create_arrays(array_count):
    if(array_count == 0):
        titles_array = []
        return titles_array
    elif(array_count == 1):
        artists_array = []
        return artists_array
    elif(array_count == 2):
        countries_array = []
        return countries_array
    elif(array_count == 3):
        prices_array = []
        return prices_array
    elif(array_count == 4):
        years_array = []
        return years_array
    else:
        print("something went wrong")


def edit_arrays(xmldoc, a, titles_array, artists_array,
                countries_array, prices_array, years_array):
    for x in range(0, a):
        title = xmldoc.getElementsByTagName("TITLE")[x].firstChild.data
        titles_array.append(title)
        artist = xmldoc.getElementsByTagName("ARTIST")[x].firstChild.data
        artists_array.append(artist)
        country = xmldoc.getElementsByTagName("COUNTRY")[x].firstChild.data
        countries_array.append(country)
        price = xmldoc.getElementsByTagName("PRICE")[x].firstChild.data
        prices_array.append(price)
        year = xmldoc.getElementsByTagName("YEAR")[x].firstChild.data
        years_array.append(year)


def get_average_price(prices_array):
    total = 0
    for count in range(0, len(prices_array)):
        total = total + float(prices_array[count])
    average_price = round((total / len(prices_array)), 2)
    average_price = str(average_price)
    return average_price


def display_results(xmldoc, a, titles_array, artists_array,
                    countries_array, prices_array,
                    years_array, average_price):
    results_count = a
    a = str(a)
    for x in range(0, results_count):
        print(titles_array[x] + " - " + artists_array[x] + " - " +
              countries_array[x] + " - " + prices_array[x] + " - " +
              years_array[x])
    print("There are " + a + " CDs in the catalog. " +
          "The average price is $" + average_price + ".")


def main():
    array_count = 0
    from xml.dom import minidom
    xmldoc = minidom.parse("cd_catalog.xml")
    a = check_amounts(xmldoc)
    for array_count in range(0, 5):
        if(array_count == 0):
            titles_array = create_arrays(array_count)
        elif(array_count == 1):
            artists_array = create_arrays(array_count)
        elif(array_count == 2):
            countries_array = create_arrays(array_count)
        elif(array_count == 3):
            prices_array = create_arrays(array_count)
        elif(array_count == 4):
            years_array = create_arrays(array_count)
        else:
            print("something went wrong")
    edit_arrays(xmldoc, a, titles_array, artists_array,
                countries_array, prices_array, years_array)
    average_price = get_average_price(prices_array)
    display_results(xmldoc, a, titles_array, artists_array,
                    countries_array, prices_array,
                    years_array, average_price)


main()
