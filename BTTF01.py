import datetime
import tkinter as tk

time1 = "1985/10/26, 01:21"
formatted_time1 = datetime.datetime.strptime(time1, "%Y/%m/%d, %H:%M")
print(formatted_time1)

time3 = "1985/10/26, 01:20"
formatted_time3 = datetime.datetime.strptime(time3, "%Y/%m/%d, %H:%M")

class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    # ウィンドウ
    master.title("デロリアン タイムサーキッド")
    self.pack(fill="both", expand=True)

    # 1-1「MONTH」の文字
    self.month_string01 = tk.Label(self,
                                  bg="#000000", # fire brick
                                  font=("Gill Sans", 30),
                                  text="MONTH",
                                  fg="#d3d3d3"
                                )
    self.month_string01.grid(row=1,
                            column=1,
                            padx=1,
                            sticky="s")

    # 1-2 blank1-2
    self.blank1_2 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank1_2.grid(row=1,
                      column=2,
                      padx=1,
                      sticky="s"
                    )

    # 1-3「DAY」の文字
    self.day_string01 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="DAY",
                                fg="#d3d3d3"
                              )
    self.day_string01.grid(row=1,
                          column=3,
                          padx=1,
                          sticky="s"
                        )

    # 1-2 blank1-4
    self.blank1_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank1_4.grid(row=1,
                      column=4,
                      padx=1,
                      sticky="s"
                    )

    # 1-5「YEAR」の文字
    self.year_string01 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="YEAR",
                                fg="#d3d3d3"
                              )
    self.year_string01.grid(row=1,
                          column=5,
                          padx=1,
                          sticky="s"
                        )
    # 1-6 blank1_6
    self.blank1_6 = tk.Label(self,
                            bg="#000000",
                            font=("", 10),
                            text="",
                            fg="#000000"
                          )
    self.blank1_6.grid(row=1,
                      column=6,
                      padx=1,
                      sticky="s"
                    )
    # 1-7「HOUR」の文字
    self.hour_string01 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="HOUR",
                                fg="#d3d3d3"
                              )
    self.hour_string01.grid(row=1,
                            column=7,
                            sticky="s"
                          )
    # 1-8 blank1_8
    self.blank1_8 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank1_8.grid(row=1,
                      column=8,
                      sticky="s"
                    )

    # 1-9「MIN」の文字
    self.min_string01 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="MIN",
                                fg="#d3d3d3"
                              )
    self.min_string01.grid(row=1,
                          column=9,
                          sticky="s"
                        )

    # 2-1「MONTH01」の14セグメント
    self.month_seg01 = tk.Label(self,
                                bg="#000000",
                                font=("DSEG14 Classic", 90, "bold"),
                                fg="red"
                                )
    self.month_seg01.grid(row=2,
                          column=1,
                          sticky="s")

    # 2-2 blank2-2
    self.blank2_2 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank2_2.grid(row=2,
                      column=2,
                      sticky="s"
                    )

    # 2-3「DAY01」の7セグメント
    self.day_seg01 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="red"
                            )
    self.day_seg01.grid(row=2,
                        column=3,
                        sticky="s")

    # 2-4 blank2-4
    self.blank2_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank2_4.grid(row=2,
                      column=4,
                      sticky="s"
                    )

    # 2-5「YEAR01」の7セグメント
    self.year_seg01 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="red"
                            )
    self.year_seg01.grid(row=2,
                        column=5,
                        sticky="s")

    # 2-6 row=2, column=6の位置にFrameを作成
    self.frame01 = tk.Frame(self, bg="#000000")
    self.frame01.grid(row=2, column=6)
    # === DESTINATION TIME の AM/PMランプ
    self.dest_am_label = tk.Label(self.frame01, text="AM", font=("Gill Sans", 18), fg="#d3d3d3", bg="#000000")
    self.dest_am_label.pack(anchor="n")
    self.dest_am_dot = tk.Label(self.frame01, text="●", font=("Gill Sans", 30), fg="#d3d3d3", bg="#000000")
    self.dest_am_dot.pack(anchor="n")

    self.dest_pm_label = tk.Label(self.frame01, text="PM", font=("Gill Sans", 18), fg="#d3d3d3", bg="#000000")
    self.dest_pm_label.pack(anchor="n")
    self.dest_pm_dot = tk.Label(self.frame01, text="●", font=("Gill Sans", 30), fg="#d3d3d3", bg="#000000")
    self.dest_pm_dot.pack(anchor="n")

    # 2-7「HOUR01」の7セグメント
    self.hour_seg01 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="red"
                            )
    self.hour_seg01.grid(row=2,
                        column=7,
                        sticky="s")
    # 2-8 ":"の文字
    self.colon01 = tk.Label(self,
                            bg="#000000",
                            font=("", 90, "bold"),
                            text=":",
                            fg="yellow"
                            )
    self.colon01.grid(row=2,
                      column=8,
                      sticky="s")

    # 2-9「MIN01」の7セグメント
    self.min_seg01 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="red"
                            )
    self.min_seg01.grid(row=2,
                        column=9,
                        sticky="s")

    # 3-3「DESTINATION TIME」の文字
    self.destination_time_string = tk.Label(self,
                                            bg="#000000",
                                            font=("Gill Sans", 40),
                                            text="DESTINATION TIME",
                                            fg="#d3d3d3"
                                          )
    self.destination_time_string.grid(row=3,
                                      column=1,
                                      columnspan=9,
                                      pady=30,
                                      sticky="s")

    # 4行目は7列ともブランク
    for i in range(1,8): #
      self.blank4_i = tk.Label(self,
                      bg="#000000",
                      font=("", 10),
                      text="",
                      fg="#000000"
                    )
      self.blank4_i.grid(row=4,
                        column=i,
                        padx=1,
                        sticky="s"
                      )

    # 5-1「MONTH」の文字
    self.month_string02 = tk.Label(self,
                                  bg="#000000", # fire brick
                                  font=("Gill Sans", 30),
                                  text="MONTH",
                                  fg="#d3d3d3"
                                )
    self.month_string02.grid(row=5,
                            column=1,
                            padx=1,
                            sticky="s")

    # 5-2 blank5-2
    self.blank5_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank5_4.grid(row=5,
                      column=2,
                      sticky="s"
                    )

    # 5-3「DAY」の文字
    self.day_string02 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="DAY",
                                fg="#d3d3d3"
                              )
    self.day_string02.grid(row=5,
                          column=3,
                          padx=1,
                          sticky="s"
                        )

    # 5-4 blank5-4
    self.blank5_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank5_4.grid(row=5,
                      column=4,
                      sticky="s"
                    )

    # 5-5「YEAR」の文字
    self.year_string02 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="YEAR",
                                fg="#d3d3d3"
                              )
    self.year_string02.grid(row=5,
                          column=5,
                          padx=1,
                          sticky="s"
                        )

    # 5-6 blank5_6
    self.blank5_4 = tk.Label(self,
                            bg="#000000",
                            font=("", 10),
                            text="",
                            fg="#000000"
                          )
    self.blank5_4.grid(row=5,
                      column=6,
                      padx=1,
                      sticky="s"
                    )
    # 5-7「HOUR」の文字
    self.hour_string02 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="HOUR",
                                fg="#d3d3d3"
                              )
    self.hour_string02.grid(row=5,
                            column=7,
                            sticky="s"
                          )
    # 5-8 blank5_8
    self.blank5_8 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank5_8.grid(row=5,
                      column=8,
                      sticky="s"
                    )
    # 5-9「MIN」の文字
    self.min_string02 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="MIN",
                                fg="#d3d3d3"
                              )
    self.min_string02.grid(row=5,
                          column=9,
                          sticky="s"
                        )

    # 6-1「MONTH02」の14セグメント
    self.month_seg02 = tk.Label(self,
                                  bg="#000000",
                                  font=("DSEG14 Classic", 90, "bold"),
                                  fg="#00ff00"
                                )
    self.month_seg02.grid(row=6,
                          column=1,
                          sticky="s")

    # 6-2 blank6-2
    self.blank1_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank1_4.grid(row=6,
                      column=2,
                      sticky="s"
                    )
    # 6-3「DAY02」の7セグメント
    self.day_seg02 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="#00ff00"
                            )
    self.day_seg02.grid(row=6,
                        column=3,
                        sticky="s")
    # 6-4 blank6-4
    self.blank6_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank6_4.grid(row=6,
                      column=4,
                      sticky="s"
                    )
    # 6-5「YEAR02」の7セグメント
    self.year_seg02 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="#00ff00"
                            )
    self.year_seg02.grid(row=6,
                        column=5,
                        sticky="s")

    # 6-6 row=6, column=6の位置にFrameを作成
    self.frame02 = tk.Frame(self, bg="#000000")
    self.frame02.grid(row=6, column=6)
    # === PRESENT TIME の AM/PMランプ
    self.pres_am_label = tk.Label(self.frame02, text="AM", font=("Gill Sans", 18), fg="#d3d3d3", bg="#000000")
    self.pres_am_label.pack(anchor="n")
    self.pres_am_dot = tk.Label(self.frame02, text="●", font=("Gill Sans", 30), fg="#d3d3d3", bg="#000000")
    self.pres_am_dot.pack(anchor="n")

    self.pres_pm_label = tk.Label(self.frame02, text="PM", font=("Gill Sans", 18), fg="#d3d3d3", bg="#000000")
    self.pres_pm_label.pack(anchor="n")
    self.pres_pm_dot = tk.Label(self.frame02, text="●", font=("Gill Sans", 30), fg="#d3d3d3", bg="#000000")
    self.pres_pm_dot.pack(anchor="n")

    # 6-7「HOUR02」の7セグメント
    self.hour_seg02 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="#00ff00"
                            )
    self.hour_seg02.grid(row=6,
                        column=7,
                        sticky="s")
    # 6-8 ":"の文字
    self.colon02 = tk.Label(self,
                            bg="#000000",
                            font=("", 90, "bold"),
                            text=":",
                            fg="yellow"
                            )
    self.colon02.grid(row=6,
                      column=8,
                      sticky="s")

    # 6-9「MIN02」の7セグメント
    self.min_seg02 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="#00ff00"
                            )
    self.min_seg02.grid(row=6,
                        column=9,
                        sticky="s")
    # 7-3「PRESENT TIME」の文字
    self.present_time_string = tk.Label(self,
                                        bg="#000000",
                                        font=("Gill Sans", 40),
                                        text="PRESENT TIME",
                                        fg="#d3d3d3"
                                      )
    self.present_time_string.grid(row=7,
                                  column=1,
                                  columnspan=9,
                                  pady=30,
                                  sticky="s")

    # 8行目は7列ともブランク
    for i in range(1,8): #
      self.blank8_i = tk.Label(self,
                      bg="#000000",
                      font=("", 10),
                      text="",
                      fg="#000000"
                    )
      self.blank8_i.grid(row=8,
                        column=i,
                        padx=1,
                        sticky="s"
                      )

    # 9-1「MONTH」の文字
    self.month_string03 = tk.Label(self,
                                  bg="#000000", # fire brick
                                  font=("Gill Sans", 30),
                                  text="MONTH",
                                  fg="#d3d3d3"
                                )
    self.month_string03.grid(row=9,
                            column=1,
                            padx=1,
                            sticky="s")
    # 9-2 blank9-2
    self.blank9_2 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank9_2.grid(row=9,
                      column=2,
                      sticky="s"
                    )
    # 9-3「DAY」の文字
    self.day_string03 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="DAY",
                                fg="#d3d3d3"
                              )
    self.day_string03.grid(row=9,
                          column=3,
                          padx=1,
                          sticky="s"
                        )
    # 9-4 blank9-4
    self.blank9_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank9_4.grid(row=9,
                      column=4,
                      sticky="s"
                    )
    # 9-5「YEAR」の文字
    self.year_string03 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="YEAR",
                                fg="#d3d3d3"
                              )
    self.year_string03.grid(row=9,
                          column=5,
                          padx=1,
                          sticky="s"
                        )
    # 9-6 blank9_6
    self.blank9_6 = tk.Label(self,
                            bg="#000000",
                            font=("", 10),
                            text="",
                            fg="#000000"
                          )
    self.blank9_6.grid(row=9,
                      column=6,
                      padx=1,
                      sticky="s"
                    )
    # 9-7「HOUR」の文字
    self.hour_string03 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="HOUR",
                                fg="#d3d3d3"
                              )
    self.hour_string03.grid(row=9,
                            column=7,
                            sticky="s"
                          )
    # 9-8 blank9_8
    self.blank9_8 = tk.Label(self,
                        bg="#000000",
                        font=("Gill Sans", 30),
                        text="",
                        fg="#000000"
                      )
    self.blank9_8.grid(row=9,
                      column=8,
                      sticky="s"
                    )
    # 9-9「MIN」の文字
    self.min_string03 = tk.Label(self,
                                bg="#000000",
                                font=("Gill Sans", 30),
                                text="MIN",
                                fg="#d3d3d3"
                              )
    self.min_string03.grid(row=9,
                          column=9,
                          sticky="s"
                        )

    # 10-1「MONTH03」の14セグメント
    self.month_seg03 = tk.Label(self,
                                  bg="#000000",
                                  font=("DSEG14 Classic", 90, "bold"),
                                  fg="yellow"
                                )
    self.month_seg03.grid(row=10,
                          column=1,
                          sticky="s")
    # 10-2 blank10-2
    self.blank10_2 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank10_2.grid(row=10,
                      column=2,
                      sticky="s"
                    )
    # 10-3「DAY03」の7セグメント
    self.day_seg03= tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="yellow"
                            )
    self.day_seg03.grid(row=10,
                        column=3,
                        sticky="s")
    # 10-4 blank10-4
    self.blank10_4 = tk.Label(self,
                        bg="#000000",
                        font=("", 10),
                        text="",
                        fg="#000000"
                      )
    self.blank10_4.grid(row=10,
                      column=4,
                      sticky="s"
                    )
    # 10-5「YEAR03」の7セグメント
    self.year_seg03 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="yellow"
                            )
    self.year_seg03.grid(row=10,
                        column=5,
                        sticky="s")

    # 10-6 row=10, column=6の位置にFrameを作成
    self.frame03 = tk.Frame(self, bg="#000000")
    self.frame03.grid(row=10, column=6)
    # === LAST TIME DEPARTED の AM/PMランプ
    self.last_am_label = tk.Label(self.frame03, text="AM", font=("Gill Sans", 18), fg="#d3d3d3", bg="#000000")
    self.last_am_label.pack(anchor="n")
    self.last_am_dot = tk.Label(self.frame03, text="●", font=("Gill Sans", 30), fg="#d3d3d3", bg="#000000")
    self.last_am_dot.pack(anchor="n")

    self.last_pm_label = tk.Label(self.frame03, text="PM", font=("Gill Sans", 18), fg="#d3d3d3", bg="#000000")
    self.last_pm_label.pack(anchor="n")
    self.last_pm_dot = tk.Label(self.frame03, text="●", font=("Gill Sans", 30), fg="#d3d3d3", bg="#000000")
    self.last_pm_dot.pack(anchor="n")

    # 10-7「HOUR03」の7セグメント
    self.hour_seg03 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="yellow"
                            )
    self.hour_seg03.grid(row=10,
                        column=7,
                        sticky="s")
    # 10-8 ":"の文字
    self.colon03 = tk.Label(self,
                            bg="#000000",
                            font=("", 90, "bold"),
                            text=":",
                            fg="yellow"
                            )
    self.colon03.grid(row=10,
                      column=8,
                      sticky="s")

    # 10-9「MIN03」の7セグメント
    self.min_seg03 = tk.Label(self,
                              bg="#000000",
                              font=("DSEG7 Classic", 90, "bold"),
                              fg="yellow"
                            )
    self.min_seg03.grid(row=10,
                        column=9,
                        sticky="s")
    # 11-3「LAST TIME DEPARTED」の文字
    self.last_time_departed_string = tk.Label(self,
                                            bg="#000000",
                                            font=("Gill Sans", 40),
                                            text="LAST TIME DEPARTED",
                                            fg="#d3d3d3"
                                          )
    self.last_time_departed_string.grid(row=11,
                                      column=1,
                                      columnspan=9,
                                      pady=30,
                                      sticky="s")

    # 12行目は7列ともブランク
    for i in range(1,8): #
      self.blank12_i = tk.Label(self,
                      bg="#000000",
                      font=("", 10),
                      text="",
                      fg="#000000"
                    )
      self.blank12_i.grid(row=12,
                        column=i,
                        padx=1,
                        sticky="s"
                      )

    # コロンの表示状態を保持するフラグ
    self.colon_visible = True

    # update関数の呼び出し
    master.after(50, self.update)

    # 行と列のサイズをリサイズ可能にする
    for i in range(1, 36): # row 1〜36
      self.grid_rowconfigure(i, weight=1)
    for i in range(1, 8): # column 1〜7
      self.grid_columnconfigure(i, weight=1)

  def update(self):
    # DESTINATION TIME
    year_part01 = formatted_time1.strftime("%Y") # 年
    month_part01 = formatted_time1.strftime("%b").upper() # 月（JAN, FEB,...）
    day_part01 = formatted_time1.strftime("%d") # 日付
    hour_part01 = formatted_time1.strftime("%I") # 時間
    min_part01 = formatted_time1.strftime("%M") # 分
    self.year_seg01.configure(text=year_part01)
    self.month_seg01.configure(text=month_part01)
    self.day_seg01.configure(text=day_part01)
    self.hour_seg01.configure(text=hour_part01)
    self.min_seg01.configure(text=min_part01)

    # PRESENT TIME
    now = datetime.datetime.now()
    year_part02 = now.strftime("%Y") # 年
    month_part02 = now.strftime("%b").upper() # 月（JAN, FEB,...）
    day_part02 = now.strftime("%d") # 日付
    hour_part02 = now.strftime("%I") # 時間
    min_part02 = now.strftime("%M") # 分
    self.year_seg02.configure(text=year_part02)
    self.month_seg02.configure(text=month_part02)
    self.day_seg02.configure(text=day_part02)
    self.hour_seg02.configure(text=hour_part02)
    self.min_seg02.configure(text=min_part02)

    # LAST TIME DEPARTED
    year_part03 = formatted_time3.strftime("%Y") # 年
    month_part03 = formatted_time3.strftime("%b").upper() # 月（JAN, FEB,...）
    day_part03 = formatted_time3.strftime("%d") # 日付
    hour_part03 = formatted_time3.strftime("%I") # 時間
    min_part03 = formatted_time3.strftime("%M") # 分
    self.year_seg03.configure(text=year_part03)
    self.month_seg03.configure(text=month_part03)
    self.day_seg03.configure(text=day_part03)
    self.hour_seg03.configure(text=hour_part03)
    self.min_seg03.configure(text=min_part03)

    # DESTINATION TIME のAM/PM 更新
    if formatted_time1.hour < 12:
      self.dest_am_dot.configure(fg="yellow")
      self.dest_pm_dot.configure(fg="#d3d3d3")
    else:
      self.dest_am_dot.configure(fg="#d3d3d3")
      self.dest_pm_dot.configure(fg="yellow")

    # PRESRENT TIME のAM/PM 更新
    if now.hour < 12:
      self.pres_am_dot.configure(fg="yellow")
      self.pres_pm_dot.configure(fg="#d3d3d3")
    else:
      self.pres_am_dot.configure(fg="#d3d3d3")
      self.pres_pm_dot.configure(fg="yellow")

    # LAST TIME DEPARTED のAM/PM 更新
    if formatted_time3.hour < 12:
      self.last_am_dot.configure(fg="yellow")
      self.last_pm_dot.configure(fg="#d3d3d3")
    else:
      self.last_am_dot.configure(fg="#d3d3d3")
      self.last_pm_dot.configure(fg="yellow")

    # コロン点滅処理
    if self.colon_visible:
      self.colon01.configure(text=":", fg="yellow")
      self.colon02.configure(text=":", fg="yellow")
      self.colon03.configure(text=":", fg="yellow")
    else:
      self.colon01.configure(text=":", fg="#000000")
      self.colon02.configure(text=":", fg="#000000")
      self.colon03.configure(text=":", fg="#000000")
    self.colon_visible = not self.colon_visible

    # 1秒ごとに更新
    self.master.after(500, self.update)

def main():
  root = tk.Tk()
  # 画面サイズを取得
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()
  print(f"screen size of the device: {screen_width} x {screen_height}")

  # フルスクリーン表示
  # root.overrideredirect(True) # ウィンドウ装飾なし
  root.geometry(f"{screen_width}x{screen_height}")
  root.attributes("-fullscreen", True)

  # escボタンで解除
  root.bind("<Escape>", lambda e: root.destroy())
  # マウスが動くと解除
  root.bind("<Motion>", func=lambda x: root.destroy())
  # 何かキーを押すと解除
  root.bind("<Key>", lambda e: root.destroy())
  app = Application(master=root)
  app.config(bg="#000000")
  app.mainloop()

if __name__ == "__main__":
  main()