from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
# def theme_default() -> Bar:
#     c = (
#         Bar()
#         # 等价于 Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
#         .add_xaxis(Faker.choose())
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .add_yaxis("商家C", Faker.values())
#         .add_yaxis("商家D", Faker.values())
#         .set_global_opts(title_opts=opts.TitleOpts("Theme-default"))
#     )
#     return c
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["0", "1", "2", "3", "4", "5", "6"], n)
    .add_yaxis("Proposed Model", [72, 739, 5179, 18344, 20736, 7055, 1210],
               # category_gap="50%",
               gap="0%")
    .add_yaxis("Null Model", [72, 195, 1091, 3025, 7226, 12528, 14517],
               # category_gap="50%",
               gap="0%", )
    .set_global_opts(
        # title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
        # toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(orient='vertical', pos_right="10%", pos_top="5%")
        )
)
# bar.render()
make_snapshot(snapshot, bar.render(), "bar.png")
