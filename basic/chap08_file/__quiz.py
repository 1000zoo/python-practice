for i in range(1,6):
    report_txt = open("quiztext/" + str(i) + "주차.txt", "w", encoding="utf8")
    report_txt.write("-" + str(i) + "주차 주간 보고-")
    report_txt.write("\n부서: ")
    report_txt.write("\n이름: ")
    report_txt.write("\n업무 요약: ")
    report_txt.close()


# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")