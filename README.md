# Net Result Surface Plot Model

Enter score, risk, and odds for 4 wagers: over, under, favorite, dog.<br>
Calculate net-result for 144 total point / spread pairings (12x12).<br>
Display 3D surface plots with spread(x-axis), total-points(y-axis), and net-result(z-axis).<br>


requirements
-
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Mpl_toolkits.mplot3d](https://matplotlib.org/3.2.1/api/toolkits/mplot3d.html)



nr_input.py
-

1a) Define lambda function 'g' for calculating 'win' for each wager.<br>
1b) Enter input variables (score/odds/risk) for each wager.<br>
1c) Create variables to define ranges for total point / spread axis'.<br>
1d) Calculate 'win' values with lambda function 'g'.<br>
1e) Print score, risk, and win for each wager. (toggle on/off with 'disp' variable)

nr_results.py
-

2a) Import nr_input, Create spread and total point DataFrames, add step 1c range variables to each df.<br>
2b) Create lists of monetary results for each wager.<br>
2c) Add lists from step 2b to df's from step 2a, calculate net-spread and net-total-points.<br>
2d) Create simple lists of net-spread / net-total-point values.<br>
2e) Create 12 x 12 Numpy array of net-result (net_map).<br>

nr_surf.py
-

3a) Import nr_input & nr_results, create matplotlib figure, add 4 subplots displayed 2x2.<br>
3b) Create 'x' and 'y' variables; assign values from range variables (in step 1c) to 'x' and 'y'.<br>
3c) Use 'x' and 'y' to create Numpy meshgrid 'X, Y'. Assign net_map (step 2e) to 'Z'.<br>
3d) Create colormap 'mycmap'. For each axis: add titles and create surf-plot.<br>
3e) Assign view angle to each axis using 'view_init(elevation, azimuth)'<br>
3f) Display matplotlib figure with 'plt.show()'<br>
<br>
<br>

Visit [Abovetb.com](https://www.abovetb.com/)
-
