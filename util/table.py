def print_table(data):
    # 각 열의 최대 너비를 저장할 리스트 초기화
    max_width_by_columns = [max([len(str(row[column_index])) for row in data]) for column_index in range(len(data[0]))]

    # 데이터 출력
    for row in range(len(data)):
        for column in range(len(data[row])):
            # ljust()를 사용해서 각 열의 너비를 최대 너비와 같도록 맞추어 출력
            print(str(data[row][column]).ljust(max_width_by_columns[column]), end="")
            # 마지막 열이 아니면 두 칸 띄워서 출력
            if column != len(data[row]) - 1:
                print("  ", end="")
        # 모든 열을 출력했으면 다음 행
        print("")
