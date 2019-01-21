import { TrainingsResponse, Training } from '../../types';

export function getTrainings(resp: TrainingsResponse): TrainingsResponse {
    resp.results = resp.results.map(x => {
        x.isExpanded = false;
        return x;
    });
    return resp;
}
