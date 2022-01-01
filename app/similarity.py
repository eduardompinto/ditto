import io
from fastapi.datastructures import UploadFile
from fastapi.params import File
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def generate_similarity_xlsx(file: UploadFile) -> io.BytesIO:
    df = pd.read_csv(io.StringIO(str(file.file.read(), 'utf-8')))
    # Uses the first column as identifier
    identifier = df.iloc[:, 0]
    # Drop the identifier column from the dataframe
    df.drop(columns=[identifier.name], inplace=True)
    similarity = cosine_similarity(df)
    sim_df = pd.DataFrame(data=similarity)
    # Adds the identifier to the similarity df
    sim_df.index = identifier
    sim_df.columns = identifier
    stream = io.BytesIO()
    sim_df.to_excel(stream)
    return stream