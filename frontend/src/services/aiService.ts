import api from "./api";

import type {
  AIAnalysis,
} from "../types/ai";

export const aiService = {

  async analyze(
    payload: Record<string, unknown>
  ): Promise<AIAnalysis> {

    const response =
      await api.post<AIAnalysis>(
        "/ai/analyze",
        payload
      );

    return response.data;
  },

};