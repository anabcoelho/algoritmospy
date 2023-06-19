def salvar_csv (classe, results, headers):
    import csv

    with open(rf'{classe}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                            quoting=csv.QUOTE_ALL, escapechar='\\')
        writer.writerow(headers)
        writer.writerows(results)
    print('salvo')
