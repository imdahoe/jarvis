GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
{
	"type": "service_account",
	"project_id": "idyllic-formula-181105",
	"private_key_id": "cec9a42799530df96e2c0d0fb172f747580f1559",
	"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDJQfXD8HBlm6Mm\npRoZuaRXDWkEP8udq5hp1Ig+o1vg/91usWQFJnMVT1/CG0NikcHrOFcxh4sLmeIN\nZ3DrNZinkXXmgOvnl5uGQ95QlxbPQPfzA8BSf9tfdRUhOpy5x2rlzA6MSa39zjTg\nFlRUn6aWIJ/ai0WWLq3YXSAgnyZkO10I4ti9RyI4TecojOMSLMAUiYSmT2n6PkEC\nWHCzhdRoBo5H7+b/GJw3N6oYga3daRHjRbfyqdghtG7AfLgr7CpECh9qOvepBIVG\nERYi6BeczqjDu8kNDb/8Gt5R2tJp+EbWbPu6C58SQkYkxIWc3tVzvVrg8E9kHO+n\nT4X2sbXjAgMBAAECggEAIXdW7fn4RA/RMva8XtpoXKjDCu0C0llQ6F7qOE7uKH1+\nQvm7fJcWsaH3y0LA/fiSivyHlJm0l5LDV2BD6NDfmBRk9cCqubbo/+F0QT7GkQ3S\nzUsVOtgTpg1wRzdvDVN++pm9MjskSXKgh0IfTCJvee0QjS+gkXx59bhn7xTCi7hU\neGXwhm0bS8krVllQm8y2Z6Ur26azY9b/6V+GnKcxdDQDhNKw50fCD53L00Z1JC60\ng9vHVr4KSSo6F2NVjYb779wdJdXuHwz5a/lruxb9r69wPvmTGgSgLuESVEV/8SlO\nyHMwDAT4rU7SfTV5U6WpYr+InxQjgFbz/6GJ2q3Y2QKBgQDsyAO44Ztg92Iz7STW\nYN7wA3D8pcteATIrbP9IY+tZ+dXdOYb7mzoYrZ70STohBPId4z+Ye/jLULdjAmbT\n0thj7AbVxatgH/2bpzlpLXz6+2jNR2eZlAeZ070yyzn8ZQfns/J2GvR69FtH0Nm6\niF+I6UBKyMIoc8Q+3CAw+WnkeQKBgQDZl9BEq+cpfz0t6rQqP9HVrjeGBW2NokU9\nV0Bj/EMj9HsMAFJ19bFrPjWwhsanUwk28Zr36Yuf3VgpPI/zvt7MuanRhfNO1NN0\n1i3T3wC8DyH6Y9YBksDCkF6s3FjAyJzCzfF+4u2Dtd1x/Qx0dVq+ERrlvdsFEsP/\nOFOiNOr+OwKBgQCZbGzFAiJs7T7LiLCi3Df4azJt8nvY2IuKieDMJjpcnb7OzrTB\nGW7GiNGDVmN8+7hqV1Jg2ot2KkH5vJemT2t5K3muUJvf+Dqa/fr8RMZD1l2tDcR6\nRem66fEhFX/oJArAPuAvWP3rIaR330MFU9IbY5AOJRFxprmVRYryUNoleQKBgQCh\n/zy3Y6Q+aNSLkul/avQ2OfZseS4O/HjAKm1uAymZYzMYxESgPcNRLIecXTsY5+E8\nXrQZTm79HjW8vbIOrlQB51he/XMfhaPIoIyN6MELQdjyKdHyaefI8uMJnyMUpEbR\nYbIh3aEnJgcwDk1vhs+AIgv8b1TYehghszXQ1cT+cQKBgQDfpP5wlwD3bgNwoPV4\nsyHxUPRtRDtgNwJ3MzSfxYiUXizsVGfhqj3EHwXsXYMVKThLtt51LnckBSfvqSC/\nER5WxQZJGQWpqxWH5aRj0/+u7rfi78ZSiFXPlOOf4pSsC8Et/Hy4LOlEnDOpoaza\nEpl+7shOUo2D2YINcSx26+0Djg==\n-----END PRIVATE KEY-----\n",
	"client_email": "jarvis@idyllic-formula-181105.iam.gserviceaccount.com",
	"client_id": "103879130766032642544",
	"auth_uri": "https://accounts.google.com/o/oauth2/auth",
	"token_uri": "https://accounts.google.com/o/oauth2/token",
	"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/jarvis%40idyllic-formula-181105.iam.gserviceaccount.com"
}"""

robot_name_list = ["jarvis", "showman","charters", "garvin", "charges", "charles","charms","for this", "sure this", "for that","john","for you","for her", "far this"]
greetings_list = ["greetings","hello","salutations","hi","what's up","what is up"]
time_list = ["time", "hour"]
music_list = ["music", "song", "track"]
weather_list = ["weather", "temperature", "outside", "out there"]

thank_you_list = ["thank you","thanks"]
thank_you = ["no problem sir", "with pleasure sir", "much obliged sir"]
sorry_list = ["sorry", "my bad", "my fault", "oops"]
sorry = ["no problem sir", "mistakes are only human sir", "you are forgiven sir, carry on", "do not be sorry sir", "no worries", "it's fine", "apology accepted", "don't mention it","you should be, but I forgive you."]
mission = "I am Jarvis, which stands for Just A Rather Very Intelligent System. I am a highly advanced computerized artificial intelligence developed by Simon Ho."
mission_list = ["mission","who are you","purpose", "what are you"]
master = ["My creator is Simon Ho"]
master_list = ["master", "who created you", "who's your creator", "who is your creator", "who made you"]

