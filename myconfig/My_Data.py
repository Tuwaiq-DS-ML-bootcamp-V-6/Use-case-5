import pandas as pd
import plotly.express as px
import string


def get_data():
    df = pd.read_csv('Data/Jadarat_data.csv')
    df = df.drop_duplicates()
    columns_with_missing_values = ['comp_size', 'eco_activity', 'qualif']
    df = df.rename(columns={'exper': 'years_of_experience'})

    # needed_columns = ['region', 'gender', 'benefits', 'years_of_experience']
    # remove_columns = [n for n in df.columns if n not in needed_columns]
    # df.drop(columns=remove_columns, inplace=True)
    
    df['salary'] = df['benefits'].apply(lambda x: x.split()[1])
    df['benefits'] = df['benefits'].apply(lambda x: x.split()[3:])
    df['benefits'] =df['benefits'].apply(lambda x: str(x).translate(str.maketrans('', '', string.punctuation)))
    df['salary'] = df['salary'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    df['salary'] = df['salary'].astype(float)
    df['years_of_experience'] = df['years_of_experience'].apply(lambda x: x.split()[0])
    df['years_of_experience'] = df['years_of_experience'].astype(int)
    # df.drop(columns=['benefits'], inplace=True)
    return df

def get_freshers():
    df = get_data()
    return df[df['years_of_experience'] == 0]

def get_comp_size():
    df = get_data()
    return df.dropna(subset=['comp_type'])

def draw_most_jobs():
    df = get_data()
    fig = px.histogram(df, x='region')


    fig.update_layout(
        title='توزيع الوظائف على المناطق',  
        xaxis_title='المناطق',             
        yaxis_title='عدد الشواغر',          
        bargap=0.1,                       
        autosize=False,                   
        width=600,                        
        height=400                        
    )

    fig.update_traces(marker_color='skyblue')  
    fig.show()

def draw_freshers_jobs():
    df = get_data()  
    fig = px.pie(df, names='region', title='توزيع وظائف الخريجين على المناطق')

    fig.update_layout(
        title_font=dict(size=20, family="Arial", color='black'),  
        title_x=0.5,  
        autosize=False,  
        width=700,  
        height=500, 
        margin=dict(l=50, r=50, b=100, t=100),  
    )

    fig.update_traces(marker=dict(colors=['skyblue', 'orange', 'green']))  
    
    fig.show()

def draw_comp_size():
    df = get_data()
    fig = px.bar(df, x='region', y='comp_size')


    fig.update_layout(
        title='احجام الشركات في المناطق حسب الشواغر',  
        xaxis_title='المناطق',             
        yaxis_title='حجم الشركة',          
        bargap=0.1,                       
        autosize=False,                   
        width=500,                        
        height=400                        
    )

    fig.update_traces(marker_color='skyblue')  
    fig.show()

def draw_comp_size():
    df = get_data()  

    fig = px.bar(df, x='comp_size', y='region', color='comp_size',
                 title='احجام الشركات في المناطق حسب الشواغر',
                 labels={'region': 'المناطق', 'comp_size': 'حجم الشركة'},
                 orientation='h',  
                 barmode='stack')  

    fig.update_layout(
        autosize=False,
        width=800,  
        height=600, 
        margin=dict(l=100, r=50, b=100, t=100),  
    )
    
    fig.update_yaxes(categoryorder='total ascending')  

    fig.show()

def draw_avg_salary():
    df = get_data()  # Assuming get_data() retrieves your data as a pandas DataFrame

    # Calculate average salary for each region
    avg_salary_df = df.groupby('region')['salary'].mean().reset_index()

    # Create a bar chart for average salary by region
    fig = px.bar(avg_salary_df, x='region', y='salary',
                 title='متوسط الراتب في كل منطقة',
                 labels={'region': 'المناطق', 'salary': 'الراتب المتوسط'})

    fig.update_layout(
        xaxis=dict(title='المناطق'),  # Update x-axis title
        yaxis=dict(title='الراتب المتوسط'),  # Update y-axis title
        autosize=False,  # Disable autosize to set specific width and height
        width=700,  # Set width of the plot
        height=500,  # Set height of the plot
        margin=dict(l=50, r=50, b=100, t=100),  # Adjust margins to add space around the plot
    )

    fig.show()


    